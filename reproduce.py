"""Reproduce manuscript totals from the released observations (standard library)."""
from pathlib import Path
from itertools import product
import csv
import json

ROOT = Path(__file__).resolve().parent


def read(name):
    with (ROOT/'data'/name).open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))


def binary_counts(rows, field):
    values = [r[field] for r in rows if r.get(field) in {'0', '1'}]
    return dict(positive=sum(int(v) for v in values), assessed=len(values),
                unassessed=len(rows)-len(values))


documents = read('documents.csv')
policy = read('representations.csv')
demands = read('source_demands.csv')
trial = read('trial_narrative.csv')
m25 = read('m25_narrative.csv')
claims = read('trial_claim_occurrences.csv')
instruction = read('instruction_coverage.csv')
provenance = read('verification_provenance.csv')
completion = read('completion_dispositions.csv')
primary_docs = [r for r in documents if r['corpus_scope']=='primary']
primary_ids = {r['document_id'] for r in primary_docs}
primary = [r for r in policy if r['article_id'] in primary_ids]

assert len({r['document_id'] for r in documents}) == len(documents)
assert len({r['article_id'] for r in policy}) == len(policy)
assert all(r['ai_intervention_visible'] in {'0','1'} for r in policy)
assert all(r['permanent_visible'] in {'0','1'} for r in policy)
assert all(r['explicit_sufficient_permission_substitution'] in {'0','1'} for r in policy)
assert all(r['permanent_visible']!='1' or r['ai_intervention_visible']=='1' for r in policy)
assert len({r['text_family'] for r in primary_docs}) == len(primary_docs)
assert len(provenance)==442
assert sum(r['earlier_author_status']=='verified' for r in provenance)==415
assert sum(r['disposition']=='source checked' for r in completion)==19
assert sum(r['disposition']=='not applicable' for r in completion)==6
assert sum(r['disposition']=='evidence limit' for r in completion)==2
assert {r['article_id'] for r in instruction}=={r['article_id'] for r in trial}
assert len(instruction)==len(trial)
assert {r['article_id'] for r in claims}=={r['article_id'] for r in trial if r['rejection_present']=='1'}

paired = {d for r in primary for d in r['demand_id'].split(';') if d}
eligible_packets = {r['source_packet_id'] for r in demands
                    if r['H2_eligible']=='confirmed' and r['demand_id'] in paired}
by_stratum = {}
for stratum in ('direct_action','legal','security_incident'):
    ids={r['document_id'] for r in primary_docs if r['stratum']==stratum}
    rows=[r for r in primary if r['article_id'] in ids]
    by_stratum[stratum]=dict(texts=len(rows),
        ai_intervention_visible=sum(int(r['ai_intervention_visible']) for r in rows),
        permanent_visible=sum(int(r['permanent_visible']) for r in rows))

counts = dict(
    primary_news_texts=len(primary),
    primary_episodes=len({r['principal_episode_id'] for r in primary_docs}),
    stop_ai_news_with_context=len(policy),
    comparator_news_texts=sum(r['corpus_scope']=='comparator' for r in documents),
    known_primary_origin_clusters=len({r['origin_cluster_id'] for r in primary_docs if r['origin_cluster_id']!='UNRESOLVED'}),
    unresolved_primary_cluster_texts=sum(r['origin_cluster_id']=='UNRESOLVED' for r in primary_docs),
    source_vintage_eligible_primary_pairs=sum(int(r['source_vintage_eligible']) for r in primary),
    complete_policy_assessable_primary_pairs=sum(int(r['full_policy_assessable']) for r in primary),
    H2_confirmed_dual_eligible_paired_packets=len(eligible_packets),
    trial_aftermath_texts=len(trial),
    necessity_rejection_texts=sum(int(r['rejection_present']) for r in trial),
    rejection_claim_sources=len({r['claim_source_id'] for r in claims}),
    rejection_quoted_prosecutor_texts=len({r['article_id'] for r in claims if r['claim_issuer_type']=='quoted prosecutor'}),
    necessity_instruction_withheld_reported=sum(int(r['necessity_instruction_withheld_reported']) for r in instruction),
    m25_legal_comparison_texts=len(m25),
    m25_merits_rejection=binary_counts(m25,'rejection_present'),
    m25_decision_assignment=binary_counts(m25,'judicial_decision_assigned_to_jury'),
    policy_intervention=binary_counts(policy,'ai_intervention_visible'),
    policy_permanence=binary_counts(policy,'permanent_visible'),
    substitution_screen=binary_counts(policy,'explicit_sufficient_permission_substitution'),
    by_stratum=by_stratum)
expected=json.loads((ROOT/'results/expected_counts.json').read_text())
differences={key:dict(expected=expected.get(key),reproduced=counts.get(key))
             for key in expected.keys()|counts.keys() if expected.get(key)!=counts.get(key)}
assert not differences, json.dumps(differences,indent=2)
(ROOT/'results/reproduced_counts.json').write_text(json.dumps(counts,indent=2)+'\n')

# A sufficient-safety claim licenses B when S is true. Merely requiring safety
# does not license any resumption state. Keep these interpretations separate.
logic=[]
for build,safe,authorization in product((0,1), repeat=3):
    source_compliant = not build or (safe and authorization)
    permits_under_sufficiency = bool(build and safe)
    logic.append(dict(build=build,safe=safe,authorization=authorization,
        source_compliant=int(source_compliant),
        sufficient_safety_permission=int(permits_under_sufficiency),
        contradiction=int(permits_under_sufficiency and not source_compliant)))
assert [(r['build'],r['safe'],r['authorization']) for r in logic if r['contradiction']]==[(1,1,0)]
with (ROOT/'results/logic_truth_table.csv').open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=list(logic[0]))
    writer.writeheader();writer.writerows(logic)
print(json.dumps(counts,indent=2))
print('All manuscript totals reproduced; source judgments and verification status remain distinct.')
