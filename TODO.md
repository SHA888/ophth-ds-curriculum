# TODO

> Atomic, granular build plan for `ophth-ds-curriculum`.
> Tasks are grouped by SemVer milestone. Each task is small enough to land in a single PR.
> Format: `[ ]` open · `[x]` done · `[~]` in progress · `[-]` cancelled with rationale.

---

## Milestone `v0.1.0` — Scaffold and governance

**Goal:** repository is forkable, contributable, and CI-protected. No curriculum content yet.

- [ ] **T0.1 — Bootstrap repository**
  - [x] T0.1.1 — Initialize git, push to GitHub
  - [ ] T0.1.2 — Add `.gitignore` (Python, R, Quarto, OS, editor)
  - [ ] T0.1.3 — Add `.editorconfig`
  - [ ] T0.1.4 — Add `CHANGELOG.md` seeded with `## [Unreleased]`
- [ ] **T0.2 — Decide and commit LICENSE** *(blocks all content tasks)*
  - [ ] T0.2.1 — Compare CC BY 4.0 vs. CC BY-SA 4.0 vs. dual (CC BY + MIT/Apache-2.0 for code)
  - [ ] T0.2.2 — Document decision rationale in `ARCHITECTURE.md` § Licensing
  - [ ] T0.2.3 — Commit `LICENSE` file
  - [ ] T0.2.4 — Add SPDX header policy to `CONTRIBUTING.md`
- [ ] **T0.3 — Governance docs**
  - [ ] T0.3.1 — `CONTRIBUTING.md` (style, commit conventions, PR checklist)
  - [ ] T0.3.2 — `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1)
  - [ ] T0.3.3 — `SECURITY.md` (no secrets, no PHI, responsible disclosure)
  - [ ] T0.3.4 — GitHub issue templates (bug, content, reading-list)
  - [ ] T0.3.5 — Pull-request template with binary checklist
- [ ] **T0.4 — CI / DevSecOps gates**
  - [ ] T0.4.1 — `markdownlint-cli2` workflow on PR
  - [ ] T0.4.2 — `lychee` link-check workflow (weekly + on PR)
  - [ ] T0.4.3 — Quarto render workflow → GitHub Pages preview
  - [ ] T0.4.4 — `gitleaks` secret scan on PR
  - [ ] T0.4.5 — Branch protection: require all checks green + 1 review
  - [ ] T0.4.6 — Dependabot for GitHub Actions versions
- [ ] **T0.5 — Quarto project skeleton**
  - [ ] T0.5.1 — `_quarto.yml` with HTML + PDF formats
  - [ ] T0.5.2 — Citation handling: CSL file (Vancouver) + empty `references.bib`
  - [ ] T0.5.3 — Sidebar navigation stubs for all 6 phases
  - [ ] T0.5.4 — Landing page (`index.qmd`) mirroring `README.md`
- [ ] **T0.6 — Release `v0.1.0`**
  - [ ] T0.6.1 — Update `CHANGELOG.md`
  - [ ] T0.6.2 — Tag `v0.1.0`, draft GitHub Release notes

---

## Milestone `v0.2.0` — Phase 0 references and Phase 1 content

**Goal:** Phase 0 cross-references `mds-curriculum` correctly; Phase 1 is complete and assessable.

- [ ] **T1.0 — Phase 0 referencing**
  - [ ] T1.0.1 — `phases/00-foundation/README.qmd` explaining the reuse of `mds-curriculum` Tiers 1–2
  - [ ] T1.0.2 — Diagnostic-accuracy statistics appendix (ophthalmology-flavored examples: screening prevalence, DR grades)
  - [ ] T1.0.3 — Phase 0 assessment checklist
- [ ] **T1.1 — Phase 1 module: image as ndarray**
  - [ ] T1.1.1 — Reading: numpy array semantics, dtype, memory layout
  - [ ] T1.1.2 — Exercise: load JPEG fundus, inspect shape/dtype, save round-trip
  - [ ] T1.1.3 — Pitfalls: BGR vs. RGB, uint8 vs. float32 normalization
- [ ] **T1.2 — Phase 1 module: color spaces and preprocessing**
  - [ ] T1.2.1 — Reading: RGB, HSV, LAB, why green channel dominates for fundus
  - [ ] T1.2.2 — Exercise: implement CLAHE manually, then via OpenCV; compare
  - [ ] T1.2.3 — Pitfalls: CLAHE tile size, over-enhancement artifacts
- [ ] **T1.3 — Phase 1 module: file formats**
  - [ ] T1.3.1 — Reading: JPEG/TIFF/PNG trade-offs for fundus
  - [ ] T1.3.2 — Reading: DICOM basics (tags, transfer syntax) for ophthalmology
  - [ ] T1.3.3 — Reading: OCT vendor formats — Heidelberg `.e2e`, Topcon `.fda`, Zeiss `.img`
  - [ ] T1.3.4 — Exercise: open one sample from each vendor format using public-domain tools
  - [ ] T1.3.5 — Dataset card template (`datasets/_template.md`) — provenance, license, access, schema
- [ ] **T1.4 — Phase 1 module: perimetry as tabular data**
  - [ ] T1.4.1 — Reading: 24-2 and 30-2 grid semantics, MD, PSD, VFI
  - [ ] T1.4.2 — Exercise: parse a sample HVF XML/CSV export, compute MD by hand
- [ ] **T1.5 — Phase 1 capstone**
  - [ ] T1.5.1 — Specification: end-to-end preprocessing pipeline for a fundus image set
  - [ ] T1.5.2 — Assessment rubric (binary checklist)
- [ ] **T1.6 — Release `v0.2.0`**
  - [ ] T1.6.1 — Update `CHANGELOG.md`
  - [ ] T1.6.2 — Tag `v0.2.0`

---

## Milestone `v0.3.0` — Phase 2: classical computer vision

**Goal:** Phase 2 complete; learners can build a defensible classical baseline.

- [ ] **T2.1 — Module: filtering and morphology**
  - [ ] T2.1.1 — Reading: convolution, Gaussian, median, bilateral
  - [ ] T2.1.2 — Reading: morphological open/close/tophat
  - [ ] T2.1.3 — Exercise: optic disc localization via tophat + thresholding
- [ ] **T2.2 — Module: edge and ridge detectors**
  - [ ] T2.2.1 — Reading: Canny, Sobel, Frangi vesselness
  - [ ] T2.2.2 — Exercise: vessel segmentation on DRIVE using Frangi; report Dice/IoU
- [ ] **T2.3 — Module: optic cup-to-disc ratio**
  - [ ] T2.3.1 — Reading: CDR clinical relevance, measurement variability
  - [ ] T2.3.2 — Exercise: classical CDR pipeline on a small public set
- [ ] **T2.4 — Phase 2 capstone**
  - [ ] T2.4.1 — Specification: reproduce a classical vessel-segmentation baseline within 10% of published Dice on DRIVE
  - [ ] T2.4.2 — Rubric (binary)
- [ ] **T2.5 — Release `v0.3.0`**

---

## Milestone `v0.4.0` — Phase 3: deep learning

**Goal:** Phase 3 complete; learners can fine-tune backbones and train U-Nets with reproducibility discipline.

- [ ] **T3.1 — Module: PyTorch fundamentals (ophthalmology-flavored)**
  - [ ] T3.1.1 — Reading: tensors, autograd, modules, optimizers
  - [ ] T3.1.2 — Exercise: train a tiny CNN on a 2-class fundus subset
- [ ] **T3.2 — Module: transfer learning with `timm`**
  - [ ] T3.2.1 — Reading: ImageNet pretraining strengths and limits for medical imaging
  - [ ] T3.2.2 — Exercise: fine-tune EfficientNet/ConvNeXt on APTOS 2019 subset
- [ ] **T3.3 — Module: segmentation with MONAI**
  - [ ] T3.3.1 — Reading: U-Net architecture, loss functions (Dice, focal, compound)
  - [ ] T3.3.2 — Exercise: U-Net for vessel segmentation on DRIVE; compare to Phase 2 baseline
- [ ] **T3.4 — Module: foundation models — RETFound**
  - [ ] T3.4.1 — Reading: Zhou Y. et al. 2023 *Nature* paper, line by line
  - [ ] T3.4.2 — Exercise: extract RETFound features, train linear probe on a downstream task
- [ ] **T3.5 — Module: experimental discipline**
  - [ ] T3.5.1 — Reading: train/val/test discipline, leakage, patient-level splits
  - [ ] T3.5.2 — Reading: seed control, deterministic ops, reproducibility envelope
  - [ ] T3.5.3 — Exercise: deliberately introduce leakage, observe inflated metrics, fix
- [ ] **T3.6 — Phase 3 capstone**
  - [ ] T3.6.1 — Specification: transfer-learned DR grader on APTOS 2019; quadratic-weighted kappa ≥ published baseline
  - [ ] T3.6.2 — Rubric (binary)
- [ ] **T3.7 — Release `v0.4.0`**

---

## Milestone `v0.5.0` — Phase 4: domain projects (the canon)

**Goal:** Phase 4 complete; learners have shipped ≥3 canonical projects with TRIPOD-AI-structured reports.

- [ ] **T4.1 — Project: DR grading**
  - [ ] T4.1.1 — Dataset cards: EyePACS, APTOS 2019, Messidor-2, IDRiD
  - [ ] T4.1.2 — Walkthrough: data → model → evaluation → report
- [ ] **T4.2 — Project: OCT classification (Kermany 2018)**
  - [ ] T4.2.1 — Dataset card: Kermany OCT
  - [ ] T4.2.2 — Walkthrough: 4-class classifier, external validation on a second OCT set
- [ ] **T4.3 — Project: glaucoma (REFUGE)**
  - [ ] T4.3.1 — Dataset card: REFUGE
  - [ ] T4.3.2 — Walkthrough: disc/cup segmentation + classification head
- [ ] **T4.4 — Project: multi-label disease (ODIR-5K)**
  - [ ] T4.4.1 — Dataset card: ODIR-5K
  - [ ] T4.4.2 — Walkthrough: multi-label loss, per-class metrics, threshold calibration
- [ ] **T4.5 — Stretch project: systemic signal from fundus**
  - [ ] T4.5.1 — Reading: Poplin et al. 2018 *Nat Biomed Eng*
  - [ ] T4.5.2 — Discussion: what data would be needed to attempt a replication; access realities
- [ ] **T4.5a — Elective project: biomedical NLP on ophthalmology text** *(added v0.0.1; UCSD-informed)*
  - [ ] T4.5a.1 — Reading: clinical NLP basics; ClinicalBERT, BioBERT, scispaCy; tokenization quirks for clinical text
  - [ ] T4.5a.2 — Reading: ophthalmology-specific text sources — operative notes, OCT/fundus imaging reports, referral letters; structuring challenges
  - [ ] T4.5a.3 — Exercise: named-entity recognition on a small public ophthalmology corpus or synthetic op-note set; extract laterality, diagnosis codes, anatomical structures
  - [ ] T4.5a.4 — Exercise: rule-based + ML hybrid pipeline; compare against pure-ML baseline; reflect on regulatory implications (deterministic vs. probabilistic decisions)
  - [ ] T4.5a.5 — Pitfalls: PHI leakage, Indonesian-language clinical text (likely majority for local deployment), code-switching with English medical terms
- [ ] **T4.5b — Elective project: ophthalmology genetics & bioinformatics** *(added v0.0.1; UCSD-informed)*
  - [ ] T4.5b.1 — Reading: inherited retinal dystrophies (IRDs) — ABCA4 (Stargardt), USH2A (Usher), RPGR (X-linked RP), gene-panel testing logic
  - [ ] T4.5b.2 — Reading: AMD genetics — CFH, ARMS2, complement pathway; polygenic risk scores and their limits
  - [ ] T4.5b.3 — Reading: glaucoma genetics — MYOC, OPTN, TBK1, recent GWAS findings
  - [ ] T4.5b.4 — Exercise: variant interpretation walkthrough on a public VCF using `pyvcf3` or `cyvcf2`; ACMG classification basics
  - [ ] T4.5b.5 — Exercise: integrate a genetic risk feature with an imaging-based AMD progression model; reflect on calibration and clinical actionability
  - [ ] T4.5b.6 — Pitfalls: ancestry bias in reference databases (predominantly European), pharmacogenomic relevance to ophthalmology drugs (limited but growing)
- [ ] **T4.6 — Phase 4 capstone**
  - [ ] T4.6.1 — Specification: take one project to external validation on a second public dataset
  - [ ] T4.6.2 — Report template following TRIPOD-AI 2024 structure
  - [ ] T4.6.3 — Rubric (binary)
- [ ] **T4.7 — Release `v0.5.0`**

---

## Milestone `v0.6.0` — Phase 5: clinical translation

**Goal:** Phase 5 complete; learners can critique deployed AI and reason about regulation in Indonesian context.

- [ ] **T5.0 — Module: research ethics (standalone)** *(added v0.0.1; UCSD-informed; separated from fairness/PDP for first-class treatment)*
  - [ ] T5.0.1 — Reading: Declaration of Helsinki, Belmont Report, and how they map to clinical AI
  - [ ] T5.0.2 — Reading: IRB/Komite Etik process in Indonesian academic medical centers; retrospective image-data protocols
  - [ ] T5.0.3 — Reading: informed consent for secondary use of retinal images; broad consent vs. specific consent
  - [ ] T5.0.4 — Reading: dual-use and deployment ethics — when a screening AI's false-negative risk shifts cost to the patient
  - [ ] T5.0.5 — Exercise: draft a minimal ethics protocol for a hypothetical retrospective DR-screening study at the learner's institution
- [ ] **T5.1 — Module: reporting standards**
  - [ ] T5.1.1 — Reading: TRIPOD-AI / TRIPOD+AI 2024
  - [ ] T5.1.2 — Reading: CONSORT-AI
  - [ ] T5.1.3 — Reading: SPIRIT-AI
  - [ ] T5.1.4 — Exercise: apply TRIPOD-AI checklist to one published ophthalmology AI study
- [ ] **T5.2 — Module: FDA-cleared device case studies**
  - [ ] T5.2.1 — IDx-DR / Digital Diagnostics: pivotal trial, clearance pathway, real-world performance
  - [ ] T5.2.2 — EyeArt: similar treatment
  - [ ] T5.2.3 — Comparison: what specifically made each clearable
- [ ] **T5.3 — Module: dataset shift and fairness**
  - [ ] T5.3.1 — Reading: dataset shift taxonomy (covariate, label, concept)
  - [ ] T5.3.2 — Reading: fairness in retinal AI across skin tone, ethnicity, age
  - [ ] T5.3.3 — Exercise: stratified performance analysis on a multi-ethnic test set
- [ ] **T5.4 — Module: Indonesian regulatory layer**
  - [ ] T5.4.1 — Reading: BPOM medical device pathway for SaMD
  - [ ] T5.4.2 — Reading: Kemenkes digital health regulations (current)
  - [ ] T5.4.3 — Reading: PDP Law UU 27/2022 implications for retinal image PHI
  - [ ] T5.4.4 — Comparison: FDA SaMD vs. BPOM pathway
- [ ] **T5.4a — Module: clinical research design for AI studies** *(added v0.0.1; UCSD-informed; design ≠ reporting)*
  - [ ] T5.4a.1 — Reading: sample size and power for diagnostic-accuracy studies; per-grade subgroup analyses
  - [ ] T5.4a.2 — Reading: pragmatic trial design vs. explanatory trial design for AI deployment
  - [ ] T5.4a.3 — Reading: hybrid effectiveness-implementation trial designs (Curran 2012 framework)
  - [ ] T5.4a.4 — Exercise: write a study design memo for a hypothetical prospective AI-assisted DR screening trial; specify enrollment, comparator, primary outcome, sample size
- [ ] **T5.4b — Module: grant-writing essentials (minimal)** *(added v0.0.1; UCSD-informed; lightweight, optional for academic-track learners)*
  - [ ] T5.4b.1 — Reading: Specific Aims page structure (NIH-style) and equivalent structures for LPDP, Kemristek, Hibah Universitas
  - [ ] T5.4b.2 — Exercise: write one Specific Aims page for the learner's intended research direction; peer or mentor review
  - [ ] T5.4b.3 — Reading: budget justification basics for clinical AI projects (compute, annotation labor, regulatory)
- [ ] **T5.5 — Phase 5 capstone**
  - [ ] T5.5.1 — Specification: written critique of one FDA-cleared device's pivotal trial
  - [ ] T5.5.2 — Specification: regulatory-readiness gap analysis for Indonesian deployment
  - [ ] T5.5.3 — Rubric (binary)
- [ ] **T5.6 — Release `v0.6.0`**

---

## Milestone `v1.0.0` — Validated by a real cohort

**Goal:** at least one learner has completed all six phases end-to-end, with feedback incorporated. Per the project owner's standing rule: *Build → Works → Community*. No community outreach before this point.

- [ ] **T6.1 — First-cohort run-through**
  - [ ] T6.1.1 — Identify ≥1 pilot learner (the original ophthalmologist friend qualifies)
  - [ ] T6.1.2 — Track time-to-completion per phase
  - [ ] T6.1.3 — Track friction points and unclear sections
  - [ ] T6.1.4 — Track whether the learner ran the four channels (reading, project, paper-club, reflection) in parallel or collapsed to sequential; capture which produced better retention *(added v0.0.1)*
  - [ ] T6.1.5 — Track whether a mentor was paired; if yes, capture cadence and value; if no, capture which mentorship-substitute strategies (peer cohort, OSS community, public learning) were used *(added v0.0.1)*
- [ ] **T6.2 — Revision pass**
  - [ ] T6.2.1 — Sweep all phases for clarifications from cohort feedback
  - [ ] T6.2.2 — Update broken links and superseded references
  - [ ] T6.2.3 — Tighten rubrics based on observed ambiguities
- [ ] **T6.3 — `v1.0.0` release**
  - [ ] T6.3.1 — Announce only after working code (i.e., completed cohort) exists
  - [ ] T6.3.2 — Tag `v1.0.0`, write retrospective in `CHANGELOG.md`

---

## Out-of-scope (post-`v1.0.0`, maybe)

These are explicitly deferred. Listed here so they are not forgotten and not smuggled into earlier milestones.

- Generative models for synthetic retina (diffusion, GANs).
- LLMs in ophthalmology (clinical note summarization, patient-facing chat).
- Surgical video analysis (cataract phaco, vitrectomy).
- OCTA-specific deep learning pipelines.
- Federated learning across ophthalmology centers.
- Edge deployment on smartphone-based fundus cameras.

Any of these may become a Phase 6 if a maintainer champions it and a cohort demands it.
