# Data Science in Production — exercise progress

Lightweight tracker so you can see what is left and what you need to run it.

**Legend:** `[ ]` not started · `[~]` in progress · `[x]` done

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
- [ ] **MovieLens (weeks 5–6)**: Download [MovieLens “latest-small”](https://grouplens.org/datasets/movielens/) and unpack under `exercise_week05/data/movielens/` and `exercise_week06/data/movielens/` as the notebooks expect.
- [ ] **Instacart (week 5, optional)**: The notebook references Instacart CSVs; add them under a `data/instacart/` tree if you have the files, or skip the Instacart block and do MovieLens-only work.

---

## By week (feasible completion path)

### Week 2 — Information retrieval (Elasticsearch API)

Path: `exercise_week02/`, `exercises/w02.md`

- [ ] Run the Dev Tools / REST steps in `w02.md` in order: create index, map fields, bulk load, `match` / `match_phrase` / range queries.
- [ ] Use `bulk_post.txt` (and `get_bulk_post.py` if you prefer scripting) for bulk indexing.
- [ ] Optionally skim `02_information_retrieval_part01_lecture.pdf` and align your mapping choices with the lecture.

### Week 3 — Elasticsearch in Python

Path: `exercise_week03/elasticsearch.ipynb`

- [ ] Configure credentials and CA path at the top of the notebook; confirm ES is reachable.
- [ ] Work through: read data, build index, bulk index, and search — run cells until outputs match intent (index stats, example queries).
- [ ] Skim `03_information_retrieval_part02_lecture.pdf` for context.

### Week 4 — Learning to rank (Home Depot + LTR + RankLib)

Path: `exercise_week04/ltr_exercise.ipynb`, `readme2.18_readme.txt`

- [ ] Obtain `queries.csv` and `products.csv`; place next to the notebook.
- [ ] Index products; enable `_ltr` feature store; create the feature set; log features for query–doc pairs; export RankLib TSV.
- [ ] Train with RankLib (e.g. LambdaMART, NDCG@k); upload model to ES; run BM25 vs rescored / LTR search and compare lists.
- [ ] Use `04_information_retrieval_part03_lecture.pdf` as the conceptual backup.

### Week 5 — Recommenders part 1 (ranking + association rules)

Path: `exercise_week05/exercise01.ipynb`

- [ ] Load MovieRatings; implement “recommend 10 movies from recent ratings” with a clear notion of reliability (diversity, novelty, or confidence — as you define it).
- [ ] Association mining: vary minimum support, count frequent itemsets, run Apriori (`apyori`), interpret rules and “tail” consequents.
- [ ] If Instacart data is available, repeat a subset of the mining on baskets; else mark that slice N/A.

### Week 6 — Recommenders part 2 (content-based + LSH + CF)

Path: `exercise_week06/exercise_02.ipynb`

- [ ] Content-based: regression path; KNN with LSH — complete item profiles, LSH index, user profile, candidate ranking, rating prediction.
- [ ] Collaborative filtering section at the end of the notebook.
- [ ] Keep `exercise_week06/data/` consistent with what the notebook paths assume (including `food.com` assets if used).

### Week 7 — Lecture only in this folder

Path: `exercise_week07/07_recommender_part03_lecture.pdf`

- [ ] Read / take notes; no code notebook in repo for this week.

### Week 8 — Bandits (UCB) + simulation + replay

Path: `exercise_week08/exercise_03.ipynb` (same theme as `exercise_08.ipynb` at repo root — pick one primary copy to avoid duplicating work)

- [ ] Understand `GaussianArm` and the synthetic generator; implement the **UCB** strategy in the marked exercise cell.
- [ ] Run the simulation and replay evaluation cells; short written takeaway (what UCB does vs baselines in your run).

### Week 9 — Computational advertising

Path: `exercise_week09/exercise_04.ipynb`, `exercise_05.ipynb`, `arm_actions_exercise.pickle`

- [ ] **exercise_04**: Train/test split, replay-style evaluation on logged data (align with the notebook’s instructions).
- [ ] **exercise_05**: Revenue and expectations, simulated A/B test, statistical and practical significance; optional CTR-lift follow-up.
- [ ] Skim `09_computational_advertising_lecture.pdf` if a concept is unclear.

### Week 10 — (no `exercise_week10` in repo)

- [ ] If the course has published materials elsewhere, add your own sub-list here; otherwise skip.

### Week 11 — Docker / Redis / user activity

Path: `exercise_week11/`

- [ ] **webapp_redis**: `cd application_examples/webapp_redis` → `docker compose up` (or `docker-compose`), hit the app, confirm Redis use from `app.py` / `compose.yaml`.
- [ ] **pythonapp_compose** (frontend + backend): build and run; trace request flow in `frontend/app.py` and `backend/app.py`.
- [ ] **exercise3 / user_activity_emulator**: build image from `user_activity_emulator/Dockerfile`, run the simulator and UI; use `training_set.bz2` / `user_activity.bz2` as the exercise specifies in code comments or lecture.

### Week 12 — Kubernetes + MongoDB stack

Path: `exercise_week12/*.yaml`, `13_devops_orchestration_lecture.pdf`

- [ ] Set image names and namespaces if your cluster requires it; create secrets safely (do not commit real credentials).
- [ ] Apply `configmap.yaml`, `secret.yaml`, `mongo.yaml`, `mongoexpress.yaml` in a sensible order; verify pods, services, and ConfigMap/Secret consumption.
- [ ] Cross-check with the orchestration lecture PDF for expected architecture.

---

## Suggested order if you are short on time

1. Weeks 2–3 (single ES setup unlocks most of IR).  
2. Week 5 (data download + ranking + Apriori).  
3. Week 6 (largest notebook — split across days).  
4. Week 8 then 9 (self-contained, no ES).  
5. Week 4 when you have CSVs + RankLib + LTR plugin time.  
6. Weeks 11–12 (containers/orchestration).

---

## Session log (optional)

| Date | Focus | Notes |
|------|--------|--------|
|      |        |        |

Add a row when you finish a week or hit a blocker (e.g. missing data file name).
