# Data Science in Production — exercise progress

Lightweight tracker so you can see what is left and what you need to run it.

**Legend:** `[ ]` not started · `[~]` in progress · `[x]` done

For every week that ships a **lecture PDF**, the **tail slides** spell out the exercise. The table below is distilled from the last 1–4 pages of each PDF; use it to confirm your notebooks cover the spec.

---

## Lecture PDFs — last-slide exercise spec vs this repo

| Week | PDF | What the end of the deck asks for | In this repo | Gaps / notes |
|------|-----|-------------------------------------|-------------|--------------|
| 2 | `exercise_week02/02_information_retrieval_part01_lecture.pdf` (pp. 9–10) | Kibana, digitized **books** CSV; 9 steps: index 3/2, sample doc, `GET` mapping, delete, **custom** mapping (full-text: author+title; filter: country, language, year), `refresh_interval`, bulk (slide: **10** books), `_count`, then **match**, **match_phrase/exact**, **range** on years. | `w02.md`, `bulk_post.txt`, `get_bulk_post.py` | Slide bulk size **10**; repo example ends at **100** docs. |
| 3 | `exercise_week03/03_information_retrieval_part02_lecture.pdf` (p. 11) | **In Python** / Jupyter: exercises **A through G**; **assignment:** index the full set with **IDs**; **title+author** full-text; **country+language** exact/keyword; **query:** works published **1850–1890** in **England** (e.g. poems / titles per lecture). | `elasticsearch.ipynb` (sections mark EXERCISE A–G; assignment in later cells) | You need the **book CSV** on disk as used in class; align credentials + CA path. |
| 4 | `exercise_week04/04_information_retrieval_part03_lecture.pdf` (pp. 24–27) | LTR path: feature store, feature logging, RankLib, **load model** into ES, **re-rank** (plain `sltr` vs `match`+`rescore`+`sltr`). p. 27 is **“Dive in!”** (reflection: train/test, static signals, BM25, NDCG@K, metrics in sklearn) — not a new lab step. | `ltr_exercise.ipynb`, `readme2.18_readme.txt` | Needs `queries.csv`, `products.csv` + **Java** RankLib + **LTR** plugin. |
| 5 | `exercise_week05/05_recommender_part01_lecture.pdf` (p. 23) | **MovieLens:** recommend **10** movies from **recent** ratings, make recommendations **reliable** (how you define it). **Instacart:** itemsets for **varying** support, pick sensible **min_support**, **association rules**, find rule whose **consequent** has **least** support (tail). | `exercise_week05/exercise01.ipynb` | **Instacart** CSVs are not in this repo; MovieLens **ml-latest-small** may need download. |
| 6 | `exercise_week06/06_recommender_part02_lecture.pdf` (pp. 25–28) | **Assignment 2 — content-based (MovieLens):** user profile, **10** candidate movies, tags and/or **genres**, **KNN** for predicted ratings on those 10; can start **small** dataset. LSH steps: item profiles → **LSH** index → user profile → query LSH → (step 5 variant in slide) user-side LSH for neighbor-based rating estimate. **Assignment 3 — CF:** **user–user** with **RMSE** across **K**, use **Surprise** (`scikit-surprise`, needs C build tools). | `exercise_week06/exercise_02.ipynb` | Regenerate **food.com** / data paths as needed. CF section should use **Surprise** as in the slide. |
| 7 | `exercise_week07/07_recommender_part03_lecture.pdf` (p. 19) | **Assignment:** on MovieLens with train/test, compare **RMSE** of: **popularity** (damped/recency), **content-based** (tags or genres), **neighborhood** CF, **model-based** CF (**SVD**, **NMF**). | *No week-7 `.ipynb` in this folder* | Treat as a **separate** notebook or report; follow the slide’s methods. |
| 8 | `exercise_week08/08_recommender_part04_lecture.pdf` (p. 19) | **Exercise:** implement **UCB**; test with **replay** on a **synthetic** dataset. | `exercise_week08/exercise_03.ipynb` (and duplicate `exercises/exercise_08.ipynb`) | Pick **one** copy; avoid doing the work twice. |
| 9 | `exercise_week09/09_computational_advertising_lecture.pdf` (p. 24) | **A/B:** simulated **revenue** lift, vary parameters (sample size, significance); **repeat** for **CTR** lift. **Contextual bandits:** **LinearUCB**-style with a library; **rewrite replay** for contextual; **Pandas &lt; 2.0** if needed. | `exercise_05.ipynb` (A/B, CTR), `exercise_04.ipynb` (contextual + replay with `mabwiser`) | Match library/version notes; keep env isolated if you pin old **pandas**. |
| 12 | `exercise_week12/13_devops_orchestration_lecture.pdf` (p. 37) | **Exercise:** run **mongo + mongo-express**; optional **K8s** for **sentiment** and **RecSys** “from last week”; no **volumes**; point Python **user simulator** at K8s **service names**; **feedback** module logs to **stdout** on each tuple; **push** three images to **Docker Hub**; **inspect** feedback pod **logs**; **scale** RecSys **1 → 2** replicas. | `exercise_week12/*.yaml` (mongo, mongo-express, config, secret) | **Large** capstone; other pieces live in **week 11** Docker/RecSys material; you must author extra manifests if you mirror the full slide. |

---

## One-time environment (do this before the notebooks that need it)

- [x] **Python**: Create a venv; install per-notebook needs (e.g. `exercise_week06/requirements.txt`, `pandas`, `elasticsearch==8.11.1`, `apyori`, Jupyter).
- [x] **Elasticsearch (weeks 2–4)**: Local ES 8.x (Docker is fine). Note TLS cert path and `elastic` user password; plug them into the notebooks (replace placeholder sections).
- [ ] **Java + RankLib (week 4)**: JRE and `RankLib-2.18.jar` in `exercise_week04/` (see `readme2.18_readme.txt`). LTR also needs the Elasticsearch LTR plugin compatible with your ES version.
- [ ] **Kubernetes (week 12)**: `kubectl` + a cluster (`minikube`, `kind`, or cloud); apply manifests from `exercise_week12/`.
- [ ] **Docker (week 11)**: For `compose.yaml` under `exercise_week11/application_examples/`.

---

## Data you may need to add (not all ship with this repo)

- [ ] **Home Depot LTR (week 4)**: `queries.csv` and `products.csv` for `ltr_exercise.ipynb` (from course materials; not present in the repo snapshot).
- [ ] **MovieLens (weeks 5–7)**: Download [MovieLens “latest-small” (and optionally larger)](https://grouplens.org/datasets/movielens/) and unpack under `exercise_week05/data/movielens/`, `exercise_week06/data/movielens/`, and for week-7 your own project folder as needed.
- [ ] **Instacart (week 5, optional)**: The notebook references Instacart CSVs; add them under a `data/instacart/` tree if you have the files, or skip the Instacart block and do MovieLens-only work.
- [ ] **Book CSV (weeks 2–3)**: Use the course `exercise.zip` dataset where the PDFs point.

---

## By week (feasible completion path)

### Week 2 — Information retrieval (Elasticsearch API)

**Lecture (tail):** `02_information_retrieval_part01_lecture.pdf` — 9-point Kibana checklist + book CSV.  
**Repo:** `exercise_week02/w02.md`, `bulk_post.txt`, `get_bulk_post.py`

- [x] All nine items: index 3/2, one doc, `GET` mapping, delete, custom mapping (author+title **text**; country, language, year for filtering), `refresh_interval: -1`, bulk, `_count`, then **match**, **match_phrase** (exact phrase), **range** on `year` — `w02.md` includes a range example.
- [x] Bulk: `bulk_post.txt` / `get_bulk_post.py` (repo uses **100** lines; slide may say 10).
- [x] Optional: skim the PDF for custom mappings, DocValues, query DSL.

### Week 3 — Elasticsearch in Python

**Lecture (tail):** `03_information_retrieval_part02_lecture.pdf` — Exercises **A–G** in Jupyter; **assignment** (full index with IDs, field types, one combined query, e.g. **England** + year window + **poem** / title rules).  
**Repo:** `exercise_week03/elasticsearch.ipynb`

- [ ] Exercises **A through G** (search / aggregations / combined queries as marked in the notebook).
- [ ] **Assignment** cells: full dataset, **ID**-based indexing, **title+author** analyzed, **country+language** for exact filters, and the **England** + year-range style query the notebook specifies (the lab text uses a concrete year band — follow the notebook and lecture).
- [ ] Configure ES credentials, CA, and the path to the **books** CSV.
- [ ] Skim the PDF for **fuzzy**, **aggregations**, and **termvectors** (covered in slides before the exercise; supports A–G).

### Week 4 — Learning to rank (Home Depot + LTR + RankLib)

**Lecture (tail / pipeline):** `04_information_retrieval_part03_lecture.pdf` — LTR: load model, re-rank with `sltr` and with `rescore` + `sltr`; last page is **Dive in!** reflection questions.  
**Repo:** `exercise_week04/ltr_exercise.ipynb`, `readme2.18_readme.txt`

- [ ] Obtain `queries.csv`, `products.csv` next to the notebook; ES + LTR plugin + `RankLib-2.18.jar`.
- [ ] End-to-end: index → `_ltr` feature set → log features → RankLib export → **train** → **upload** model → **BM25** result list vs **rescore**+LTR list; optionally answer **Dive in!** questions in a short write-up.
- [ ] If `products.csv` / `queries.csv` are missing, you cannot run the full notebook — secure them from the course.

### Week 5 — Recommenders part 1 (ranking + association rules)

**Lecture (tail):** `05_recommender_part01_lecture.pdf` p. 23 — MovieLens + Instacart tasks as in the table above.  
**Repo:** `exercise_week05/exercise01.ipynb`

- [ ] **MovieLens:** **10** recent-rating–based recs with an explicit “reliability” argument; implement as in the notebook.
- [ ] **Instacart (if you have data):** support sweeps, reasonable **min_support**, Apriori rules, **tail** consequent.
- [ ] If no Instacart, complete MovieLens and note N/A for baskets.

### Week 6 — Recommenders part 2 (content-based + LSH + CF)

**Lecture (tail):** `06_recommender_part02_lecture.pdf` — **Assignment 2** (content + KNN + LSH, 10 movies, tags/genres), **Assignment 3** (user–user, RMSE vs **K**, **Surprise**).  
**Repo:** `exercise_week06/exercise_02.ipynb`, `requirements.txt`

- [ ] **Content + LSH** track: item profiles, LSH, user profile, recommend and predict ratings (steps line up with slides pp. 25–26 and the **Assignment 2** blurb on p. 25).
- [ ] **CF with Surprise** (KNN, cross-val **RMSE**): as in p. 28; install `scikit-surprise` and ensure a working **C** toolchain (see slide).
- [ ] **Food.com** / `movielens` data paths: match the notebook; small MovieLens is fine for a first pass.

### Week 7 — Model comparison (lecture only in repo)

**Lecture (tail):** `07_recommender_part03_lecture.pdf` p. 19 — compare **RMSE** of popularity vs content-based vs neighborhood vs **SVD/NMF** (Surprise) on a train/test split.  
**Repo:** *no* `exercise_week07/*.ipynb` here.

- [ ] New notebook or script: same comparison structure as the slide; cite MovieLens split and metrics.
- [ ] Reuse patterns from `exercise_02.ipynb` / Surprise docs; no need to wait for a handout file that may not exist in git.

### Week 8 — Bandits (UCB) + simulation + replay

**Lecture (tail):** `08_recommender_part04_lecture.pdf` p. 19 — **UCB** + **replay** on **synthetic** data.  
**Repo:** `exercise_week08/exercise_03.ipynb` (prefer this path; `exercise_08.ipynb` duplicates the topic)

- [ ] Implement **UCB**; run **simulation** and **replay**; compare to baselines the notebook provides.

### Week 9 — Computational advertising (A/B + contextual bandits)

**Lecture (tail):** `09_computational_advertising_lecture.pdf` p. 24 — **A/B** on **revenue**; repeat for **CTR**; **contextual** bandit (**LinearUCB**-style) + **contextual replay**; **pandas** version note.  
**Repo:** `exercise_week09/exercise_04.ipynb`, `exercise_05.ipynb`, `arm_actions_exercise.pickle`

- [ ] **exercise_05:** power / sample size-style setup, run **A/B** on **revenue**; then **CTR** block (p. 24 “replicate (almost) the same workflow”).
- [ ] **exercise_04:** contextual **mabwiser** (or as instructed), then **contextual replay**; if versions fight, use a venv with **Pandas &lt; 2.0** as the slide says.

### Week 10 — (no `exercise_week10` in repo)

- [ ] If the course publishes a PDF or notebook later, add a row to the table above and a subsection here.

### Week 11 — Docker / Redis / user activity (no dedicated lecture PDF in this list)

- [ ] `application_examples/webapp_redis/`, `pythonapp_compose/`, `exercise3/user_activity_emulator/` as before — supports **week 12** RecSys + simulator paths when you wire K8s.

### Week 12 — DevOps & orchestration (K8s)

**Lecture (tail):** `13_devops_orchestration_lecture.pdf` p. 37 — full list: mongo+mongo-express, optional sentiment+RecSys deploys, no **volumes**, service **names** for the simulator, stdout on feedback, **Docker Hub** pushes, log inspection, **scale** 1→2.  
**Repo:** `exercise_week12/configmap.yaml`, `secret.yaml`, `mongo.yaml`, `mongoexpress.yaml` (+ PDF command cheatsheets on prior pages)

- [ ] **Minimum in-repo:** `kubectl apply` order (secret, configmap, mongo, mongo-express); `kubectl get all`; access mongo-express (e.g. `minikube service`); clean up.
- [ ] **Full slide spec:** build/push **three** images, wire **week-11** RecSys/simulator code to **service** names, feedback logging, **scale** deployment — will require **extra** YAML/artifacts beyond the few files here; treat as a **capstone** checklist, not a single `kubectl apply` step.

---

## Suggested order if you are short on time

1. Weeks 2–3 (one ES install).  
2. Week 5 (data download + ranking + Apriori).  
3. Week 6 (largest local notebook).  
4. Week 8 then 9.  
5. Week 4 when you have LTR data + Java + plugin.  
6. Week 7 (standalone compare-RMSE mini-project).  
7. Weeks 11 then 12 (Docker then K8s; week 12 “full” exercise pulls in week-11 code).

---

## Session log (optional)

| Date | Focus | Notes |
|------|--------|--------|
|      |        |        |

Add a row when you finish a week or hit a blocker (e.g. missing data file name).
