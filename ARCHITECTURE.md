<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Architecture

> Design rationale for `ophth-ds-curriculum`. This document explains *why* the curriculum is structured the way it is.
> It is meant to be read once, then referenced when proposing structural changes.

---

## 1. Design principles

The curriculum is itself a project, and follows the same cross-stack non-negotiables applied to software work:

| Principle | Curriculum interpretation |
|-----------|---------------------------|
| **KISS** | Each phase has one dominant idea. No phase teaches two paradigms at once. |
| **YAGNI** | No Docker, no Kubernetes, no MLOps platforms in the core path. Added only when a concrete project demands them. |
| **SoC** | Imaging foundations, classical CV, and deep learning live in separate phases — not interleaved. |
| **High cohesion / low coupling** | Phases can be skipped if prerequisites are met externally. No phase secretly depends on a later phase. |
| **SemVer** | Curriculum versions communicate breaking vs. additive changes to learners and forks. |
| **Parse-don't-validate** | Datasets are introduced with explicit schema + provenance + license metadata in a dataset card *before* code touches them. |
| **Make-illegal-states-unrepresentable** | Assessment rubrics are checklists with binary criteria, not Likert scales — ambiguity is designed out. |
| **Chesterton's Fence** | Classical CV (Phase 2) is included even though deep learning subsumes it in practice. Removing it produces learners who can't debug what CNNs learned. |
| **Boy Scout Rule** | Every reading list reviewed annually; broken links and superseded papers swept on each MINOR release. |
| **Meta-rule: CI-enforced** | Lint, link-check, and render must pass on `main`. Quality conventions without red CI are wishes. |

---

## 2. Why this structure, and not another

### 2.1 Why imaging-first instead of EHR-first

General "medical data science" curricula (including `mds-curriculum`) lead with tabular EHR data because that is where most non-radiology, non-pathology clinicians work. Ophthalmology inverts this: the clinical record is **the image**. Visual acuity and IOP are tabular and important, but the diagnostic and prognostic signal is overwhelmingly in fundus photos, OCT, OCTA, and perimetry.

Leading with EHR teaches the wrong reflexes (tidyverse-style wrangling, time-series modeling, missingness imputation) before the dominant modality.

### 2.2 Why classical CV before deep learning

Two reasons:

1. **Debugging intuition.** A learner who has hand-implemented adaptive thresholding, morphological operations, and Frangi vesselness can reason about *why* a CNN's segmentation fails. A learner who started with U-Net cannot.
2. **Resource floor.** Classical CV runs on a CPU laptop. Deep learning does not (practically). Phase 2 keeps the learner productive while they arrange GPU access for Phase 3.

The Chesterton's Fence argument applies: classical CV is unfashionable, not useless.

### 2.3 Why a tight canon

Ophthalmology AI has thousands of papers. A curriculum that lists 200 of them produces breadth without competence. The tight canon (7 primary papers + 3 reporting-standard papers) is chosen because:

- Each is highly cited *and* clinically translated or near-translation.
- Each represents a distinct lesson (large-scale supervised, external validation, triage workflow, systemic-signal surprise, regulatory clearance, benchmark dataset, foundation model).
- A learner who has read all 10 deeply has a defensible mental model of the field.

Expansion happens in `references/` as annotated bibliography, not as required reading.

### 2.4 Why Quarto instead of Jupyter Book / mdBook / Hugo

- Native R and Python execution in the same document (Phase 0 uses both).
- First-class PDF output for offline use and printing (relevant for low-bandwidth settings).
- Citation handling via CSL + BibTeX.
- Already the platform for `mds-curriculum` — consistency reduces tooling burden for shared maintainers.

### 2.5 Why `uv` instead of conda / poetry / pip-tools

- Single binary, no Python bootstrap problem.
- Lockfile + reproducible installs by default.
- Fast enough that learners don't conflate slowness with progress.
- Aligns with the parent project's tooling standard.

---

## 3. Phase contracts

Each phase declares an explicit **input contract** (what the learner must already know) and **output contract** (what the learner can do at the end). This is the curriculum's analog of a typed interface.

### Phase 0 — Foundation

- **In:** clinical training, no CS background, willingness to use a terminal.
- **Out:** can read/write Python and R, understands sensitivity/specificity/AUROC/AUPRC/calibration, can use git for solo workflows, can manage environments with `uv`.
- **Reuse:** [`mds-curriculum`](https://github.com/balinesthesia/mds-curriculum) Tier 1 + Tier 2.

### Phase 1 — Medical imaging foundations

- **In:** Phase 0 output.
- **Out:** can load fundus JPEG/TIFF and OCT vendor formats into numpy arrays, understands color spaces and CLAHE, can read DICOM where present, can handle perimetry as tabular grid.
- **Net-new:** vendor-format quirks (Heidelberg `.e2e`, Topcon, Zeiss) are domain-specific and not covered in general imaging courses.

### Phase 2 — Classical computer vision on ophthalmology data

- **In:** Phase 1 output.
- **Out:** can implement vessel segmentation with Frangi/Gabor filters, optic disc/cup with morphological ops + Hough, evaluate against DRIVE/STARE/CHASE_DB1 ground truth using Dice/IoU.
- **Capstone:** reproduce a classical vessel-segmentation baseline within 10% of published Dice on DRIVE.

### Phase 3 — Deep learning for ophthalmology

- **In:** Phase 2 output, access to a GPU (local or cloud).
- **Out:** can fine-tune `timm` backbones, train a U-Net with MONAI, use RETFound features for downstream tasks, evaluate with proper train/val/test discipline.
- **Capstone:** transfer-learned DR grader on APTOS 2019 reaching published-baseline quadratic-weighted kappa.

### Phase 4 — Domain projects

- **In:** Phase 3 output.
- **Out:** has completed ≥3 of the canonical projects (DR grading, OCT classification, glaucoma, multi-label disease, fundus-to-systemic stretch), each with a written report following TRIPOD-AI structure.
- **Capstone:** one project taken to external validation on a second public dataset.

### Phase 5 — Clinical translation

- **In:** Phase 4 output.
- **Out:** can critique a published clinical AI study using TRIPOD-AI / CONSORT-AI / SPIRIT-AI checklists, understands FDA SaMD pathway and BPOM/Kemenkes parallels, can identify fairness and dataset-shift failure modes in a deployment proposal.
- **Capstone:** written critique of one FDA-cleared device's pivotal trial, plus a regulatory-readiness gap analysis for an Indonesian deployment.

---

## 4. Assessment philosophy

- **Binary rubrics.** Each capstone is evaluated against a checklist with yes/no items. No Likert scales, no holistic scoring. This is the *make-illegal-states-unrepresentable* principle applied to grading.
- **External validation required.** Every model-building capstone (Phase 3+) requires evaluation on a held-out dataset *from a different source* than training. Internal cross-validation alone fails the rubric.
- **Reproducibility required.** Every capstone must run end-to-end from a clean clone with `uv sync` + a documented data-access step. Non-reproducible submissions fail regardless of reported metrics.
- **Written report required.** Code without a report fails. The report follows TRIPOD-AI structure from Phase 3 onward.

---

## 5. What this curriculum deliberately omits

- **MLOps tooling** (MLflow, Weights & Biases, DVC) — useful in industry, premature for learning. Mentioned in Phase 5 as awareness only.
- **Specific vendor SDKs** beyond what is needed to load images. Heidelberg/Topcon/Zeiss SDKs are touched only at the read-data layer.
- **Generative models** (diffusion, GANs for synthetic retina) — active research area but not core competence. May appear as an optional appendix post-`v1.0.0`.
- **LLMs in ophthalmology** — moving too fast to teach durably. A separate companion repo may track this if demand emerges; explicitly out of scope here. (Note: biomedical **NLP** ≠ LLMs and *is* in scope as a Phase 4 elective; see T4.5a.)
- **Surgical video analysis** — important but a distinct sub-specialty (cataract phaco, vitrectomy) with different data pipelines. Out of scope; could be a Phase 6 if a maintainer champions it.

> **Previously considered for omission, now included as Phase 4 electives** (informed by review of UCSD Ophthalmology Informatics & Data Science Fellowship coursework, which names biomedical NLP and bioinformatics as foundational):
>
> - **Biomedical NLP on ophthalmology text** — operative notes, imaging reports, referral letters. Tractable for self-study and clinically applicable. See `TODO.md` T4.5a.
> - **Ophthalmology genetics & bioinformatics** — inherited retinal dystrophies (ABCA4, USH2A, RPGR), AMD complement pathway, glaucoma loci. Pragmatic introduction, not a substitute for a formal bioinformatics program. See `TODO.md` T4.5b.

---

## 6. Failure modes to watch

These are the ways this curriculum could go wrong, listed so future maintainers can recognize them early:

1. **Phase bloat.** Each phase grows until completion takes 6 months instead of 8 weeks. Mitigation: hard word-count budgets per phase, enforced at PR review.
2. **Reading-list creep.** Canon expands from 10 to 50 papers. Mitigation: additions require removing an existing paper (zero-sum).
3. **Tool churn.** Curriculum chases each new framework. Mitigation: tooling changes require a MAJOR version bump and a written rationale.
4. **Loss of clinical anchor.** Curriculum drifts toward generic computer vision. Mitigation: every exercise must use an ophthalmology dataset or be removed.
5. **Implicit GPU assumption.** Curriculum becomes inaccessible to learners without GPU access. Mitigation: Phases 0–2 must remain CPU-feasible; Phase 3+ must document cloud-GPU alternatives.

---

## 7. Relationship to `mds-curriculum`

- **Shared:** Phase 0 (foundation). Maintained upstream in `mds-curriculum`; this repo references it rather than vendoring.
- **Diverged:** Phases 1–5 are net-new and ophthalmology-specific.
- **Not shared back:** changes here do not flow back to `mds-curriculum` unless they are genuinely modality-neutral (rare).

A potential future refactor: extract Phase 0 into a third repo (`med-ds-foundation`) that both curricula depend on. Deferred until a third sibling curriculum emerges and the duplication becomes painful — *YAGNI*.

---

## 8. Comparison to mentored fellowship models (UCSD reference)

Informed by review of the [UC San Diego Ophthalmology Informatics & Data Science Fellowship](https://oph.ucsd.edu/education/fellowships/ophthalmology-informatics-data-science.html). The comparison is illustrative; UCSD's program is one of several mentored models and is not held up as the only valid pedagogy.

| Dimension | UCSD mentored fellowship | This self-study curriculum | Verdict |
|---|---|---|---|
| Structure | Parallel: coursework + seminars + JC + committee + research, concurrent | Phase-gated spine with parallel intra-phase channels (see README § Learning model) | **Adopted intra-phase parallelism;** kept linear spine because self-learners need prerequisite-gating that mentors otherwise provide. |
| Coverage breadth | Twelve named courses spanning informatics, NLP, bioinformatics, stats, ethics, grant writing, research design | Five phases focused on imaging + clinical translation; NLP and genetics as Phase 4 electives | **Deliberate narrower spine.** Imaging-first is the right opinionated stance for ophthalmology self-study; breadth available via electives. |
| Mentorship | Load-bearing: PD + faculty mentors + committee chairs | Optional pairing; pay-it-forward "next mentor" pedagogy from `mds-curriculum` when no mentor available | **Honest framing.** Not a constraint, but the path itself in LMIC contexts. |
| Operational/governance exposure | Direct (CDS Committee, AI Committee, HIS Medical Directors) | Replaced by published implementation case studies in Phase 5 | **Honest substitute.** Reading about deployment ≠ being in the room, and the curriculum says so. |
| Credentialing | Optional master's stack (MAS Clinical Research, MS Data Science, MS Health Informatics) | None; pointer in README to external pathways | **Orthogonal.** Curriculum produces competence; credentialing is a separate decision. |
| Funding pooling | T15 NLM + T32 NEI + ACGME Clinical Informatics | N/A | Out of scope. |
| Research ethics | Standalone course | Phase 5 module (T5.0, separated from fairness/PDP per UCSD signal) | **Adopted.** Worth its own slot. |
| Clinical research design | Standalone course | Phase 5 module (T5.4a, separated from reporting standards per UCSD signal) | **Adopted.** Design ≠ reporting. |
| Grant writing | Standalone practicum | Phase 5 minimal module (T5.4b: specific aims page exercise) | **Adopted in minimal form.** Useful for academic-track learners; lightweight enough not to bloat the spine. |
| Biomedical NLP | Foundational course | Phase 4 elective project (T4.5a) | **Adopted as elective.** Not core spine; available for learners with text-rich data access. |
| Bioinformatics | Foundational course | Phase 4 elective project (T4.5b) | **Adopted as elective.** Same rationale. |

The pattern: this curriculum is a **narrower, opinionated, mentor-optional spine** with elective branches. UCSD is a **wider, breadth-first, mentor-mandatory** model. Different goals, both legitimate.

---

## 9. Mentorship-substitute strategies

A mentor cannot be replicated by a curriculum. But several substitute structures, in decreasing order of effectiveness, can carry parts of the load:

1. **Peer cohort** — two or more learners moving through the phases together, with a fixed weekly meeting. Forces verbalization, surfaces misunderstandings, creates accountability. Cheapest and most effective substitute. Recommended minimum: one co-learner.
2. **OSS community participation** — contributing to MONAI, `timm`, Hugging Face medical-imaging discussions, or domain-specific repos (RETFound, REFUGE evaluation tooling). Submitting issues, reviewing PRs, writing examples. Build → Works → Community: contribute only when you have working understanding, not before.
3. **Public learning** — writing up each phase's lessons in a blog or GitHub repo. Imposes an external audience pressure that approximates a mentor's critical eye. Subject to vanity-metric trap; mitigate by tracking depth (citations earned, questions received) not reach (views, stars).
4. **Structured paper-club, one-person edition** — one paper per fortnight, written critique posted publicly. Forces engagement deeper than reading.
5. **Project demo deadlines** — pre-announce a date by which a project will be demonstrable (to peer cohort, local department, or an online community). External commitment substitutes for mentor accountability.

### 9.1 The pay-it-forward axis

Borrowed from `mds-curriculum`: every learner who completes the curriculum becomes a candidate mentor for the next learner. In a context where institutional mentors in clinical informatics are scarce (true of most of Indonesia outside a handful of academic centers), this is not a workaround — it is the only sustainable pedagogy. Each cohort produces the teaching cadre for the next, with the curriculum itself as the durable artifact.

Operationally:

- A learner approaching `v1.0.0` of their own progression should expect to mentor at least one subsequent learner.
- Mentor pairing should be lightweight: monthly check-in + on-demand paper discussion + capstone review. Not a full apprenticeship.
- Mentors are not expected to be experts beyond the next learner's current phase. Stay-one-phase-ahead is sufficient and sustainable.
-
