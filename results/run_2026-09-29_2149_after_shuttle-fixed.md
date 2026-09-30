# Run log — after_shuttle-fixed

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-29 21:49

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| How difficult is the  CS 340 Databases ? | pass | pass | pass |
| How is  Morrow house, what are good and bad? | pass | pass | pass |
| what is the wait time for Verrill Street Grill? | pass | pass | pass |
| Is campus shuttle free for students? | pass | pass | pass |
| Can i change my meal plan ? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.787 | refused |
| How do I change the oil in a diesel engine ? | 0.923 | refused |
| Who won the 1994 World Cup? | 0.847 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.824 | refused |
| How do I write a for loop in Rust? | 0.877 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### How difficult is the  CS 340 Databases ? — run 1

- Best distance: 0.3524 (passed the gate)
- Sources retrieved: course_cs_210_exams.txt, course_cs_210_workload.txt, course_cs_340.txt, course_cs_340_exams.txt, course_cs_340_workload.txt

```
Based on the provided documents, the workload for CS 340 Databases is 6 hours a week early in the term and 15 hours a week in the last three weeks when the project lands (from `course_cs_340_workload.txt`). Additionally, the course format includes lectures twice a week, a term-long project, and assessment via one midterm and a final, both of which are open-book and lightly curved by usually two or three points (from `course_cs_340.txt` and `course_cs_340_exams.txt`).
```

### How difficult is the  CS 340 Databases ? — run 2

- Best distance: 0.3524 (passed the gate)
- Sources retrieved: course_cs_210_exams.txt, course_cs_210_workload.txt, course_cs_340.txt, course_cs_340_exams.txt, course_cs_340_workload.txt

```
Based on the provided documents, the workload for CS 340 Databases is 6 hours a week early in the term and 15 hours a week in the last three weeks when the project lands (from `course_cs_340_workload.txt`). Additionally, the assessment consists of one open-book midterm and an open-book final, which are lightly curved by usually two or three points (from `course_cs_340_exams.txt` and `course_cs_340.txt`).
```

### How difficult is the  CS 340 Databases ? — run 3

- Best distance: 0.3524 (passed the gate)
- Sources retrieved: course_cs_210_exams.txt, course_cs_210_workload.txt, course_cs_340.txt, course_cs_340_exams.txt, course_cs_340_workload.txt

```
Based on the provided documents, the workload for CS 340 Databases is 6 hours a week early in the term and 15 hours a week in the last three weeks when the project lands (from `course_cs_340_workload.txt`). Additionally, the assessment consists of one midterm and a final, which are both open-book and lightly curved by usually two or three points (from `course_cs_340.txt` and `course_cs_340_exams.txt`).
```

### How is  Morrow house, what are good and bad? — run 1

- Best distance: 0.3439 (passed the gate)
- Sources retrieved: housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt

```
Morrow House was built in 1954 and partially renovated in 2008, featuring single and double rooms with hall bathrooms (`housing_morrow_house.txt`). Regarding noise, it is loud until about 1am on weekends and has no enforced quiet hours (`housing_morrow_house_noise.txt`). For laundry, there are eight washers and six dryers (costing $1.50 to wash and $1.25 to dry via coin or card), but the wrong ratio causes dryers to back up on Sunday evenings (`housing_morrow_house_laundry.txt`).
```

### How is  Morrow house, what are good and bad? — run 2

- Best distance: 0.3439 (passed the gate)
- Sources retrieved: housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt

```
Based on the provided documents, Morrow House was built in 1954 and partially renovated in 2008, featuring single and double rooms with hall bathrooms (housing_morrow_house.txt). Regarding noise, it is loud until about 1am on weekends and has no enforced quiet hours (housing_morrow_house_noise.txt). For laundry, it has eight washers and six dryers that cost $1.50 to wash and $1.25 to dry (using coin or card), but the wrong machine ratio causes dryers to back up on Sunday evenings (housing_morrow_house_laundry.txt).
```

### How is  Morrow house, what are good and bad? — run 3

- Best distance: 0.3439 (passed the gate)
- Sources retrieved: housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt

```
Based on the provided documents, Morrow House was built in 1954 and partially renovated in 2008, featuring single and double rooms with hall bathrooms (`housing_morrow_house.txt`). It is loud until about 1am on weekends and has no enforced quiet hours (`housing_morrow_house_noise.txt`), and its laundry facilities have an improper ratio of washers to dryers, causing dryers to back up on Sunday evenings (`housing_morrow_house_laundry.txt`).
```

### what is the wait time for Verrill Street Grill? — run 1

- Best distance: 0.1381 (passed the gate)
- Sources retrieved: admin_parking_permits.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
Based on the documents, the wait time for Verrill Street Grill is up to 30 minutes on Friday evenings, and otherwise under 10 minutes (*dining_verrill_street_grill.txt* and *dining_verrill_street_grill_followup.txt*).
```

### what is the wait time for Verrill Street Grill? — run 2

- Best distance: 0.1381 (passed the gate)
- Sources retrieved: admin_parking_permits.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
The wait time for Verrill Street Grill is up to 30 minutes on Friday evenings, and otherwise under 10 minutes (dining_verrill_street_grill.txt).
```

### what is the wait time for Verrill Street Grill? — run 3

- Best distance: 0.1381 (passed the gate)
- Sources retrieved: admin_parking_permits.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
The wait times for Verrill Street Grill are up to 30 minutes on Friday evenings, and under 10 minutes at other times. 

Source: `dining_verrill_street_grill.txt` (also supported by `dining_verrill_street_grill_followup.txt`).
```

### Is campus shuttle free for students? — run 1

- Best distance: 0.5009 (passed the gate)
- Sources retrieved: housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt, transit_shuttle.txt

```
Yes, the campus shuttle is free with a student ID. 
(Source: transit_shuttle.txt)
```

### Is campus shuttle free for students? — run 2

- Best distance: 0.5009 (passed the gate)
- Sources retrieved: housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt, transit_shuttle.txt

```
Yes, the campus shuttle is free with a student ID. 
(Source: transit_shuttle.txt)
```

### Is campus shuttle free for students? — run 3

- Best distance: 0.5009 (passed the gate)
- Sources retrieved: housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt, transit_shuttle.txt

```
Yes, the campus shuttle is free with a student ID (transit_shuttle.txt).
```

### Can i change my meal plan ? — run 1

- Best distance: 0.2834 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_north_kitchen.txt, dining_pellew_dining_hall.txt, dining_the_ridgeway_cafe.txt, housing_fenwick_court.txt

```
Yes, you can change your meal plan tier once during the first ten days of the semester; after that, it is locked (admin_meal_plan_changes.txt).
```

### Can i change my meal plan ? — run 2

- Best distance: 0.2834 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_north_kitchen.txt, dining_pellew_dining_hall.txt, dining_the_ridgeway_cafe.txt, housing_fenwick_court.txt

```
Yes, you can change your meal plan tier once during the first ten days of the semester, after which it is locked (admin_meal_plan_changes.txt).
```

### Can i change my meal plan ? — run 3

- Best distance: 0.2834 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_north_kitchen.txt, dining_pellew_dining_hall.txt, dining_the_ridgeway_cafe.txt, housing_fenwick_court.txt

```
Yes, you can change your meal plan tier once during the first ten days of the semester, after which it is locked (admin_meal_plan_changes.txt).
```
