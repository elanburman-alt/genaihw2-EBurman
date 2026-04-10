# Prompt Iterations

## Version 1 — Initial Prompt
"Draft a donor follow-up email based on this information."

**What changed:** Nothing yet — this is the baseline.  
**Observation:** Output was generic, no instructions on length or tone. 
Model invented details in Case 4 (hallucination problem).

---

## Version 2 — Added Role + Constraints
"You are a professional fundraiser helping draft warm, personalized donor 
follow-up emails. Do not invent facts. Keep to 3-4 paragraphs."

**What changed:** Added persona, hallucination guardrail, length constraint.  
**Improvement:** Case 4 now uses placeholders instead of invented details. 
Tone improved. Case 5 (annoyed donor) still too apologetic.

---

## Version 3 — Final Version (in app.py)
[Paste the full SYSTEM_PROMPT from your app.py here]

**What changed:** Added instruction to not over-apologize and to use 
relationship-first framing.  
**Improvement:** Case 5 much more balanced. Case 3 (no name) now produces 
a usable template. Overall tone is more authentic.