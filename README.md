# The Unofficial Guide

**Name:** Debasish Halder  
**Corpus:** campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

**Corpus Suitability**
I opted to go for campus_life. Though I tried all other corpus and had very good success rate

Content reflects real campus-life problems across admin, courses, dining, and housing.
Each question typically has at most two different answers, sometimes contradicting (good vs. bad).
Topic is clearly labeled at the top of each item.
Moderate sentence length (a couple of lines), so only a modest context window is needed.  And I can experiment quite a bit

My firs build worked for the campus life but didnot work for the Threads and city guides. so I changed the chunker as needed to work for each type and my scores got to acceptable level and the responses were grounded

## Chunking Strategy

**Chunk size:**
500 chracters (for the campus_life and advice_threads, for City_guides I used 900  )

**Overlap:**
50(i.e 10%, same for all corpus) Original chunker shortest 178 and longest 549. In view of this I kept the chunk size as 500 character so as to avoid corrupting context and kept context at paragraph boundary and allowed 10% overlap
With changed chunker i got shortest 36 longest 397

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents (original mode -> fallback_split)`

```
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents (original mode -> fallback_split)
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents (original mode -> fallback_split)`

```
======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents (original mode -> fallback_split)
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents (original mode -> fallback_split)`

```
======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents (original mode -> fallback_split)
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents (original mode -> fallback_split)`

```
======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents (original mode -> fallback_split)
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents (original mode -> fallback_split)`

```
======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents (original mode -> fallback_split)
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** "what is workload of CS 210 ?"

**Answer:**

```
The workload for CS 210 Data Structures is 8 to 10 hours a week outside class, and it is front-loaded with the first month being heavier than the rest.

Source: course_cs_210_workload.txt

Sources retrieved: course_cs_210_exams.txt, course_cs_210_workload.txt, course_cs_340_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

1 model calls this session, 584 tokens (529 in, 55 out)
```

**My relevance cutoff:**

```
(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "What is the capital of Mongolia?"
  (best distance 0.825, cutoff 0.6)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "How do I change the oil in a diesel engine?"
  (best distance 0.934, cutoff 0.6)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "Who won the 1994 World Cup?"
  (best distance 0.888, cutoff 0.6)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "What is the recommended dosage of ibuprofen for a headache?"
  (best distance 0.849, cutoff 0.6)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "How do I write a for loop in Rust?"
  (best distance 0.893, cutoff 0.6)

I don't have enough information about that.

0 model calls this session
```

The Best Distance I got was 0.337 using default chunker; using custom chunker I got 0.350.

## How I Used AI

**1.**

While Building custom chunker I used claude to give me the python code based on my ask of how I want to build chunker how specific strategies can be applied to each of the three data file types and based on their way of representing information so as I get very good context without increasing the chunk size to large level.

**2.**

I implemented the chunker which will work for all the types of data / corpus we were given. As a stretch type laterty I could add metadata based filtering and adding seprate vector space for documents which will help in city_guides kind of corpus

Here is my interaction with Claude on chunking strategy for city_guide and I was having to and fro:

**My Question:**

Can we have a vector which is specifc to a city which only has background and when we findit first finds the city name and then find the info vector and then section is a second vecotrr thereby we have only one additional vecrofor info vector which but stored in a seprate vector space

**Claude Response:**

- Yes, this is a sensible design — you're describing a narrower version of two-level retrieval that only splits out the intro/background, not the whole doc. Let me think through it carefully because it's genuinely different from what I described before, and it might actually be worth building for your setup where the fully general version wasn't.

- What you're proposing, in my words

- Two vector spaces (Chroma collections):

- Intro collection. One vector per doc, embedded from the doc's intro paragraph plus its title. For Marchwood, that's # Marchwood\n\nMarchwood is the regional hub — 180,000 people.... Around 14 vectors for city_guides.
Sections collection. One vector per section chunk, the way your _strategy_sectioned currently produces them minus the intro chunk. For Marchwood, that's 7 vectors (one per section).

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

> **Note on which criteria wording is in play.** Criteria 2, 3, 4, and 5 were revised in Week 2 (originals still visible in `criteria.md` above the revisions per the milestone's rule). All verdicts below are scored against the **revised** wording, since those are the current operative targets. Criterion 1 was not revised and is scored against its original wording.

## Run Log — Before (`results/run_2026-09-27_2246_before.md`)

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

The raw run log's per-question pass/fail table:

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| when to buy parking pass? | pass | pass | pass |
| what is the class workload for CS210? | fail | fail | fail |
| what is the wait time for Verrill Street Grill? | fail | fail | fail |
| What is the intake process to get Counselling in the health centre? | fail | fail | fail |
| Can i change my meal plan ? | fail | fail | fail |

Reading `scorer.py`'s marks literally, that's 1 of 5 per run, which would make criteria 1 and 5 MISSED at 1/5, 1/5, 1/5. But the pasted output of every "fail"-marked question shows a specific, correctly-cited, factually accurate answer — the scorer is disagreeing with reality. See Diagnoses. Per the milestone doc ("Without it those cells come out blank and you judge them yourself by reading the answers"), I re-scored by reading the pasted output directly. Both scoring views are shown below so the disagreement is evident. So the judge method written has a bug: it takes all words of **expects** in sequence with stop words, so if there is slight difference in the expects vs. the actual answer, the judge will say fail.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 1/5 (scorer) · 5/5 (direct read) | 1/5 · 5/5 | 1/5 · 5/5 | MET (by direct read) |
| 2. Every answer names a source | 5 of 5, all 3 runs | 5/5 | 5/5 | 5/5 | MET |
| 3. The relevance gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk context and sizing | 4 of 5 sample chunks | 5/5 | 5/5 | 5/5 | MET |
| 5. Accuracy of response | 4 of 5, all 3 runs | 1/5 (scorer) · 5/5 (direct read) | 1/5 · 5/5 | 1/5 · 5/5 | MET (by direct read) |

The 1/5 in scorer can be checked for the question-related scorer given above; the 5/5 is arrived at by directly reading and checking the content.

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

All question output below produced by `run_eval.py::main`, retrieval via `store.py::search`, chunks from `chunker.py::split_documents`. Out-of-scope table produced by `run_eval.py::check_out_of_scope`. Chunk sample produced by `chunker.py::split_documents` via `python app.py --corpus campus_life chunks -n 5`.

**Criterion 1 — Retrieved chunks contain the answer.** Target: *For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer.*

Pasted from run 1 of the before-run:

```
### when to buy parking pass? — run 1

- Best distance: 0.4766 (passed the gate)
- Sources retrieved: admin_parking_permits.txt, dining_halden_hall_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, transit_shuttle.txt

Student permits for the west lots go on sale in August (admin_parking_permits.txt).

### what is the class workload for CS210? — run 1

- Best distance: 0.3530 (passed the gate)
- Sources retrieved: course_biol_160_workload.txt, course_cs_210_workload.txt, course_cs_340_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

The workload for CS 210 Data Structures is 8 to 10 hours a week outside class of real time.
Source: course_cs_210_workload.txt

### what is the wait time for Verrill Street Grill? — run 1

- Best distance: 0.1381 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

The wait time for Verrill Street Grill is up to 30 minutes on Friday evenings, and otherwise under 10 minutes (dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt).

### What is the intake process to get Counselling in the health centre? — run 1

- Best distance: 0.4123 (passed the gate)
- Sources retrieved: advising_registration.txt, course_phys_130.txt, health_center.txt

Counselling is separate, located in the same building, and has its own intake process with a shorter wait than people expect, typically taking three or four days for a first session.
Source: health_center.txt

### Can i change my meal plan ? — run 1

- Best distance: 0.2834 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_north_kitchen.txt, dining_the_atrium.txt, dining_the_ridgeway_cafe.txt, housing_fenwick_court.txt

Yes, you can change your meal plan tier once during the first ten days of the semester, after which it is locked.
Source: `admin_meal_plan_changes.txt`
```

**Criterion 2 — Every answer names a source.** Target: *For every question that receives an answer (not a refusal), the system names at least one source document, and that document is one that actually contains the stated fact — 5 of 5 test questions, across all 3 runs.*

The output above shows source naming for run 1. Runs 2 and 3 use varied phrasing but every generated answer names a source. Examples from runs 2 and 3:

```
### what is the wait time for Verrill Street Grill? — run 2
Based on the documents, the wait time for Verrill Street Grill is up to 30 minutes on Friday evenings, and otherwise under 10 minutes (dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt).

### Can i change my meal plan ? — run 2
Yes, you can change your meal plan tier once during the first ten days of the semester, but after that, it is locked (admin_meal_plan_changes.txt).

### what is the class workload for CS210? — run 3
The workload for CS 210 Data Structures is 8 to 10 hours a week outside class.
Source: course_cs_210_workload.txt

### What is the intake process to get Counselling in the health centre? — run 3
Counselling has its own intake process that is separate in the same building, and it features a shorter wait than people expect, typically taking three or four days for a first session.
Source: health_center.txt
```

**Criterion 3 — The relevance gate stops out-of-corpus questions.** Target: *When I ask a question which my corpus documents don't say clearly, the relevance gate's distance check stops it before generation, and the system returns a refusal ("I don't have enough information about that") — for at least 4 of 5 out-of-corpus test questions.*

Pasted verbatim from the before-run's out-of-scope section:

```
## The relevance gate on out-of-corpus questions

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "What is the capital of Mongolia?"
  (best distance 0.787, cutoff 0.5)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "How do I change the oil in a diesel engine?"
  (best distance 0.923, cutoff 0.5)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "Who won the 1994 World Cup?"
  (best distance 0.847, cutoff 0.5)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "What is the recommended dosage of ibuprofen for a headache?"
  (best distance 0.824, cutoff 0.5)

I don't have enough information about that.

0 model calls this session

(venv-codepath) debasishhalder@Debasishs-Mac-mini codepath % python app.py --corpus campus_life ask "How do I write a for loop in Rust?"
  (best distance 0.877, cutoff 0.5)

I don't have enough information about that.
```

**5 of 5 received "I don't have enough information about that." Lowest rejected distance 0.787 vs. cutoff 0.5 — real margin, not borderline.**

**Criterion 4 — Chunk context and sizing.** Target: *Within a sample of 5 chunks, at least 4 must satisfy all of the following: the chunk does not span a paragraph boundary; it begins and ends on a sentence boundary; it is no longer than 900 characters.*

Pasted from `python app.py --corpus campus_life chunks -n 5` (183 chunks total; strategy: `prose_with_headings`):

```
======================================================================
Chunk 1 (58 words * 2 approx for token / 370 characters) |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but adrop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2 (16 words * 2 approx for token)  |  source: course_cs_340_exams.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Start the term project in week three, not week eight; everyone learns this the hard way.

======================================================================
Chunk 3 (27 words * 2 approx for token) |  source: course_phys_130_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.

======================================================================
Chunk 4 (22 words * 2 approx for token)  |  source: dining_verrill_street_grill_followup.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.

======================================================================
Chunk 5 (16 words * 2 approx for token)  |  source: housing_morrow_house.txt#1  |  produced by: chunker.py::split_documents
======================================================================
The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

Checking each chunk against the three conditions:

- **Paragraph boundary:** all 5 stay within a single paragraph. Chunks 1 and 3 visibly contain two text blocks, but each is a heading-plus-body pair that the `prose_with_headings` strategy deliberately merges to avoid orphaning one-line heading chunks — intentional pairing, not paragraph-spanning.
- **Sentence boundary begin/end:** all 5 begin on a sentence or heading, and end on `.`
- **≤900 characters:** all 5 well under. Largest is chunk 1 at ~370 chars, inside the `_HARD_MAX_CHUNK_SIZE = 900` guard in the chunker. Through visual inspection we can see the first response was the biggest and it's limited to 370 characters and our limit is approximately 900 characters (256 tokens).

5 of 5 satisfy all three conditions.

## Verdicts

<!-- 

     Milestone 2. -->

MET on all five, but criteria 1 and 5 pass only on direct read of the pasted output — the `scorer.py` judge function reports them as failing due to the paraphrase-vs-substring bug described above. So I will improve on the judge function in the next milestone

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET (direct read; scorer disagrees) | Scorer's raw table said 1/5 per run, but reading the pasted output plainly showed all 5 questions retrieved a chunk containing the answer, deterministic across runs (best distances 0.1381–0.4898, all under the 0.5 gate). Target is 4 of 5; direct read gives 5/5. MET. |
| 2 | Every answer names a source | MET | All 15 generated answers cite a source file, and each named file actually contains the fact stated in the answer. Target 5 of 5 across all 3 runs — held. |
| 3 | The relevance gate stops out-of-corpus questions | MET | 5 of 5 out-of-corpus questions refused with the required refusal string, lowest rejected distance 0.787 vs. cutoff 0.5 — real margin, not borderline. Target 4 of 5, cleared with room. |
| 4 | Chunk context and sizing | MET | 5 of 5 sampled chunks satisfy all three conditions: within one paragraph, sentence-boundary begin/end, and well under 900 characters (largest ~370). Target 4 of 5, cleared. |
| 5 | Accuracy of response | MET (direct read; scorer disagrees) | Scorer's raw table said 1/5 per run, but reading each answer against its retrieved chunks, every claim traces back to text in the source. Runs vary in what they include, not in what they add. Target 4 of 5 across all 3 runs; direct read gives 5/5. MET. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->


Every criterion MET on direct reading, so no per-criterion diagnoses. But the before-run surfaced a real problem in the scoring layer that's worth documenting, because if I'd taken the scorer's raw marks at face value I would have written up criteria 1 and 5 as MISSED at 1/5 — that's how large the gap between the automated verdict and the direct-read verdict was.

**Scorer disagreement.** *Stage: scoring, upstream of the criteria.* `scorer.py` marked 4 of 5 questions as fail/fail/fail in the before-run's table while their pasted output was factually correct and correctly cited. Root cause: `questions.py` `expects` strings were long paraphrases of the source text — sometimes with words that never appear in the source. The judge did substring matching on every word, so any paraphrased word not literally present in the model's answer failed the whole question, even when the answer was correct.

**On whether all-MET means the criteria were set low:** three of the five (1, 3, 4) cleared their targets with real margin, which suggests the underlying system is genuinely working for this corpus. Criterion 2 is set at 5/5 across all 3 runs, which is a strict target — attribution is cheap and any miss is a real bug — so MET is what "working" looks like here, not a low bar. Criterion 5 (fabrication) is the one I'd tighten in a re-write: what I actually want to catch is inconsistent recall across runs, which isn't quite the same as fabrication (see "What I'd Do Differently").


## The Improvement

**What I changed:**

Two things, both targeting the scorer disagreement above:
1. **`questions.py` — tightened `expects` strings** so each one is a short, deterministic phrase actually present in both the source document and a correct answer. Removed paraphrased words that were never in the source.
2. **`scorer.py` — improved the judge function** to remove stop words from `expects` before matching, so common words like "the," "a," "of" don't get treated as required literal hits.


**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

     My before-run's raw table said 1/5 pass rate on the questions the RAG system was actually answering correctly — a measurement problem in the scoring layer, not a system problem. Fixing retrieval or chunking wouldn't have helped, because retrieval and chunking were already MET on direct reading; the issue was entirely between the model's output and the pass/fail verdict. I picked this fix because being able to trust my own run log is a prerequisite for every future evaluation of this system — if the scorer keeps calling correct answers "fail," I can't reliably tell when something real actually breaks.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

`python run_eval.py --label after` — produced `results/run_2026-09-28_2202_after.md`.

Raw per-question pass/fail table from the after-run:

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| when to buy parking pass? | pass | pass | pass |
| what is the class workload for CS210? | pass | pass | pass |
| what is the wait time for Verrill Street Grill? | pass | pass | pass |
| What is the intake process to get Counselling in the health centre? | pass | pass | pass |
| Can i change my meal plan ? | pass | pass | pass |

The scorer now agrees with direct reading — 5 of 5 pass on every run.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5, all 3 runs | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk context and sizing | 5/5 | 5/5 | 5/5 | MET |
| 5. Accuracy of response | 4 of 5, all 3 runs | 5/5 | 5/5 | 5/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
     Yes it worked after I changed the judge method implementation and the results are deterministic to a very high degree and I have been seeing stable reponse . he before-run's automated table said 1/5, 1/5, 1/5 for criteria 1 and 5 while direct reading of the same output said 5/5, 5/5, 5/5. After the fix, the automated table and the direct read agree at 5/5. This is the change I set out to make: my diagnosis pointed at scoring, my fix touched scoring, and scoring changed.
     The generated answers themselves also happen to be slightly more stable in the after-run (counselling agrees across all 3 runs on including the wait-time detail, where the before-run had it in 2 of 3), but I can't attribute that to my change — I didn't touch the model or the prompt, and retrieval is identical between runs. That's honest run-to-run variance falling on the good side, not a proven effect of my fix.

     Initial implementation of the judge method backfired. and I was not able to get it working  and then I made sure all key words are ther ein the expects while framing the expects

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
     Nothing is broken now, but stability of one topic is still in doubt and that is in regards to Health topic on councilling.

     My fix removed stop words from `expects`, which handles the specific bug I hit. But any future question with a paraphrased `expects` — say, "up to half an hour" when the source says "up to 30 minutes" — will still fail scoring even if the answer is correct. A more robust approach would be substring matching against the retrieved chunk text rather than against a hand-written `expects` string, so the scorer checks whether the model's answer contains phrases that actually exist in the source rather than phrases I guessed at ahead of time. I stopped here because it works well enough for the current 5 questions. 

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
     I would broaden this beyond "answer is in a retrieved chunk" to also require that the top chunk (rank 1, not just top-5) is the correct one. With top-k=5 and a small corpus, containing the answer somewhere in 5 results is a low bar; the more meaningful measure is whether retrieval actually ranks the right chunk first.

     he 5-chunk sample passed cleanly, but with only 183 chunks in `campus_life` and this sample being mostly short single-paragraph documents, the sample didn't really stress-test the packing or overlap logic in the chunker. I'd tighten this to sample from long documents specifically (where the chunker actually has to make interesting cuts), or increase the sample to 15-20 chunks drawn randomly across the corpus, so the criterion measures the chunker's hardest cases rather than its easiest ones.

     Accuracy of responses- this is the one I'd most change. My current wording checks for fabrication (does the answer add anything not in the retrieved chunks), which is the right thing to check for grounding — and it passed cleanly. But what my run logs also surfaced, that this criterion couldn't catch, is that the model produces different subsets of the same source paragraph across runs with identical retrieved chunks. That's a consistency problem, not a fabrication problem, and it deserves its own criterion. I would split this into two: (a) no fabrication (the current one, keep as is), and (b) consistency — the set of facts stated across the 3 runs should be equivalent, not just individually grounded. Criterion (a) would have MET on the before-run; criterion (b) would have MISSED on counselling, which is a more honest picture of what I saw.




