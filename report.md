# Report: GenAI Donor Follow-Up Email Prototype

## Business Use Case

Frontline fundraisers and major gifts officers at healthcare organizations 
spend significant time drafting personalized donor follow-up emails after 
meetings, events, and cultivation conversations. Each email must balance 
warmth, specificity, and a clear — but not heavy-handed — call to action. 
The quality of these communications directly affects donor retention and 
major gift conversion. This prototype explores whether a large language 
model can serve as a reliable first-draft assistant for this workflow, 
reducing drafting time while preserving relational tone.

The system receives brief structured notes about a donor interaction — 
name, context, giving interest, and ask level — and produces a 3-4 paragraph 
follow-up email. The intended user is a gift officer who reviews and 
personalizes the draft before sending.

## Model Choice

I used Google Gemini 2.5 Flash via the Google AI Studio API and the 
`google-genai` Python library. Gemini 2.5 Flash was selected for its 
availability on a paid Google API account, its strong instruction-following 
capability, and its low latency for iterative testing. Earlier attempts 
using `gemini-2.0-flash` and `gemini-1.5-flash` failed due to model 
deprecation on newer API accounts. The `google.generativeai` package was 
also deprecated during this project, requiring a full migration to the 
newer `google.genai` SDK — itself a useful real-world lesson in how quickly 
AI tooling changes.

No alternative models were formally benchmarked, though earlier outputs 
produced under Version 1 and Version 2 prompts using the same model provided 
a meaningful internal comparison across prompt iterations.

## Baseline vs. Final Design

The prompt evolved through three versions, each producing meaningfully 
different outputs across the five evaluation cases.

| Dimension | Version 1 (Baseline) | Version 3 (Final) |
|---|---|---|
| Tone | Generic, template-like | Warm, professional, specific to AHC |
| Organization identity | None — placeholders throughout | Adventist HealthCare named explicitly |
| Sender identity | [Your Name] placeholder | Signs as Elan Burman, AVP of Philanthropy |
| Hallucination risk (Case 4) | Invented husband details in some runs | Uses general language; avoids fabrication |
| Edge case handling (Case 3) | Produced usable but fully generic output | Filled in AHC pediatric context naturally |
| Difficult donor (Case 5) | Overly apologetic; sycophantic tone | Acknowledges friction without groveling |

The most significant improvement came from adding organizational identity 
and role context in the system prompt. Once the model understood it was 
writing as a named professional at a specific institution, the outputs 
stopped using generic placeholders like [Organization Name] and began 
producing emails that actually sounded like they came from Adventist 
HealthCare. Subject lines also improved substantially in relevance and tone.

## Where the Prototype Still Fails

Two persistent failure modes require mandatory human review. First, Case 4 
(named gift in memory of a late spouse) remains risky: the model sometimes 
produces language that implies prior knowledge of the husband's name or 
professional background that was never provided. While Version 3 reduced 
this tendency, the model cannot reliably distinguish between inferring 
plausible details and inventing them. Any email involving grief, legacy 
giving, or highly personal donor history must be reviewed before sending.

Second, the model consistently produces emails that are slightly longer and 
more formal than what a seasoned gift officer would actually send. The 
natural, conversational warmth of a peer-to-peer major gifts relationship 
is difficult to replicate from a brief input note. The prototype produces 
a solid structural scaffold, not a finished letter.

## Deployment Recommendation

I would recommend this prototype for deployment as a **first-draft assistance 
tool only**, under the following conditions:

1. Every output is reviewed and edited by the gift officer before sending — 
   no autonomous sending under any circumstances.
2. The tool is clearly labeled as AI-assisted within any internal workflow 
   documentation.
3. Cases involving bereavement, named gifts, donor complaints, or sensitive 
   personal circumstances are flagged for enhanced review.
4. The system prompt is updated when organizational priorities, program names, 
   or institutional voice standards change.

Used under these conditions, the prototype offers genuine value: it reduces 
the cognitive load of starting from a blank page, ensures structural 
completeness, and handles routine cases — like post-meeting follow-ups and 
planned giving introductions — with reasonable quality. It is not a 
replacement for relationship judgment, institutional knowledge, or the 
authentic voice that distinguishes great fundraising correspondence.