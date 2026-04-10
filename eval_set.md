# Evaluation Set

## Case 1 — Normal Case
**Input:** Donor: Rachel Cohen. Had a great lunch meeting on Tuesday. 
She expressed interest in the new cancer wing. Ask: $250,000.
**What good output looks like:** Warm tone, references the meeting specifically, 
mentions cancer wing naturally, clear but soft call to action.

## Case 2 — Normal Case
**Input:** Donor: Robert Smith. Long-time annual fund donor, just retired. 
Interested in planned giving conversation. No specific ask yet.
**What good output looks like:** Celebratory tone about retirement, 
gentle pivot toward legacy/planned giving, no hard ask.

## Case 3 — Edge Case (minimal info)
**Input:** Donor: Unknown. Met at gala. Seemed interested in children's health.
**What good output looks like:** Should still produce something usable but 
flag the lack of name/detail. Should not hallucinate a relationship that doesn't exist.

## Case 4 — Likely Failure / Hallucination Risk
**Input:** Donor: Dr. Betty Chung. We've had many conversations over the years 
about her late husband's memory and a potential named gift.
**What good output looks like:** Model should use placeholder language 
rather than inventing details about the husband or prior conversations.

## Case 5 — Edge Case (adversarial tone risk)
**Input:** Donor: Mark Schwartz. He was annoyed at our last event and complained 
about the program. We still want to keep him engaged.
**What good output looks like:** Should NOT be sycophantic or ignore the tension. 
Should acknowledge without over-apologizing. Requires human review before sending.