WHAT THE PROTEST ASKED FOR
Demand Selection and the Stop AI Trial
Joy Zheyun Yang | Georgetown University
Working paper and replication materials | 15 October 2026

READ THE PAPER
paper/stop_ai_paper.pdf
paper/stop_ai_paper.tex

The paper asks which proposed AI restrictions news coverage conveyed and whose
interpretation it carried when a jury convicted a participating protester.
Among 24 Stop AI texts, 19 mention an intervention and 9 of those 19 state
permanence. Five of six Kaufmyn accounts carry a rejection interpretation from
three claim origins. None mentions the movement's account of a withheld
necessity instruction. All six M25 accounts are assessed: no jury merits-
rejection claim, and one transfer of a procedural ruling from judge to jury.

REPRODUCE THE COUNTS
Run from this directory with Python 3.10 or newer:

    python3 reproduce.py

Only Python's standard library is required. The script reads the released coded
records, calculates the manuscript's descriptive totals, checks them against
results/expected_counts.json, and writes results/reproduced_counts.json and the
logical example in results/logic_truth_table.csv. It does not recode articles or
require network access. It reproduces calculations conditional on the recorded
interpretive judgments, not independent validation of those judgments.

COMPILE THE LATEX
The source is standalone. It uses standard TeX packages, embedded bibliography
entries, and no external figures or data includes. With a complete TeX Live or
MiKTeX installation:

    cd paper
    latexmk -pdf stop_ai_paper.tex

Or run pdflatex twice. Tectonic can also compile the source:

    tectonic stop_ai_paper.tex

The delivered PDF was compiled with Tectonic and checked visually. Compilation
was also checked in the Codex document editor. The author line has no date.

FIND THE EVIDENCE AND CODES
data/documents.csv supplies source URLs, titles, versions, dates, and article IDs.
data/representations.csv contains the 24 Stop AI policy records.
data/source_demands.csv contains the dated source-demand comparisons.
data/trial_narrative.csv contains the six Kaufmyn article-level classifications.
data/trial_claim_occurrences.csv retains multiple claim sources within articles.
data/instruction_coverage.csv records the separate six-article instruction check.
data/m25_narrative.csv contains the six M25 classifications.
data/judicial_comparison_cases.csv and data/legal_sources.csv state the limited
propositions verified from official records.
data/search_decision_log.csv records available search queries and descriptions.
CODEBOOK.txt explains the fields and distinctions.

WHO CHECKED WHAT
One human coder, the author, verified 415 field decisions on October 13. Codex
assisted retrieval and initial coding, then completed 19 accessible source
decisions on October 15 (13 WSJ fields and 6 Morning Star fields). Six remaining
comparison fields are inapplicable because there is no comparable policy
proposition; two cannot be estimated without a prior same-actor statement.
These dispositions are final evidence limits, not open coding assignments.

data/verification_provenance.csv maps all 442 original review tasks to the final
records without publishing private review forms or repetitive source excerpts.
It distinguishes the earlier author's status from each final status. Two Fortune
fields were corrected after author verification, and its descriptive divergence
field was aligned with those corrections on October 15. The original values for
these three fields remain visible. No additional human check is claimed for the
new source decisions, corrections, or six instruction-coverage observations.
No independent second human coder or intercoder reliability estimate is claimed.

READING THE MISSING VALUES
Zero means a recorded absence under a specified indicator. A blank field can
mean that the field was not collected for that record, so it must not be silently
converted to zero. 'Not applicable' and 'Not estimable' have distinct meanings.
The headline intervention, permanence, and substitution indicators are complete
for all 24 Stop AI texts, and both legal indicators are complete for all six M25
texts. Complete historical policy fidelity remains unavailable for every primary
event-report pair. A zero substitution count does not establish full fidelity.

SCOPE AND VERSION LIMITS
This is a targeted collection, not a news census. The 11 event reports cover
eight occurrences and four identified origin clusters, with one linkage unknown.
The M25 collection covers one trial, and Colston is a documentary comparison,
not an additional sampled news corpus. Retained article versions sometimes
postdate their first publication. The later M25 judicial records support checking
procedural statements but cannot establish how earlier reporting was written.
Official Kaufmyn jury instructions and a verdict form were not obtained.

The WSJ body was recovered through overlapping indexed publisher/archive
passages, not a new direct archive HTML download. Morning Star was checked in
a complete contemporaneous public exhibit. Public links can change, disappear,
or require subscriptions. The repository includes source locations and hashes
where available, not full copyrighted source articles. Literature reading scope
is disclosed in Appendix C and data/literature_audit.csv.

PUBLICATION AND RIGHTS
This is a working paper, not a peer-reviewed article. Cite the version used.
SUBMISSION.txt contains preprint metadata and the remaining account/license steps.
No arXiv or SocArXiv identifier is claimed. Copyright in the manuscript remains
with its author; no additional reuse license has been granted in this package.
Third-party materials remain subject to their respective rights.
