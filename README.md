# Ophthalomology Data Science Curriculum

> A self-learner curriculum for computer science, informatics, and data science applied to **ophthalmology**.
> Designed for clinically-trained ophthalmologists with no formal CS/informatics background.

**Status:** `v0.0.1` — scaffolding. No content yet. LICENSE pending discussion (see [§ Licensing](#licensing)).

---

## Why this exists

Ophthalmology is one of the most imaging-saturated specialties in medicine: fundus photography, OCT, OCTA, ultra-widefield imaging, perimetry, anterior-segment imaging. It is also one of the most active subfields in clinical AI — first FDA-cleared autonomous AI (IDx-DR, 2018), first retinal foundation model (RETFound, 2023).

A clinician entering this space needs a learning path that is:

1. **Imaging-first**, not EHR-first (unlike most general "medical data science" curricula).
2. **Evidence-anchored** — each phase points to peer-reviewed canon, not blog posts.
3. **Translation-aware** — reporting standards (TRIPOD-AI, CONSORT-AI), regulatory paths (FDA, BPOM, Kemenkes), and dataset-shift concerns are first-class, not afterthoughts.
4. **Achievable on a constrained machine** — laptop-friendly, with cloud GPU as opt-in.

This curriculum is the ophthalmology-specific sibling of [`mds-curriculum`](https://github.com/balinesthesia/mds-curriculum) (anesthesia/ICU). The **Phase 0 foundation overlaps**; everything from Phase 1 onward diverges.

---

## Target learner

- Trained ophthalmologist (resident, fellow, or consultant).
- Comfortable reading English medical literature.
- No assumed CS background, but willing to spend ~5–10 h/week for 12–18 months.
- Owns a laptop capable of running Linux (native or WSL2) with ≥16 GB RAM. GPU optional until Phase 3.

This curriculum is **not** a substitute for:
- A formal MS/PhD in biomedical informatics.
- A clinical-research methods course (epidemiology, biostatistics).
- Direct mentorship for first-author publications.

It is a **structured self-study scaffold** to reach the point where mentorship and formal coursework become useful.

---

## Learning model

This curriculum is organized as **phases** (linear spine, prerequisite-gated), but within each phase the learner runs **four channels in parallel**, not sequentially. Pedagogy borrowed in part from mentored fellowship models (e.g., UCSD Ophthalmology Informatics & Data Science Fellowship), adapted for self-study:

1. **Reading channel** — the phase's primary papers and references, dripped weekly.
2. **Project channel** — hands-on exercise that runs the full length of the phase, not just at the end.
3. **Paper-club channel** — one paper per fortnight, discussed (with a peer, mentor, or written in public).
4. **Reflection channel** — short weekly write-up: what stuck, what didn't, what to revisit.

Running these in parallel is the difference between *finishing the syllabus* and *learning the material*. Strict sequential consumption (read everything → then do exercise → then read paper) is a known failure mode.

## Learning path

| Phase | Title | Focus | Typical duration |
|------:|-------|-------|------------------|
| 0 | Foundation | Linux, git, Python (uv), R, numpy/pandas, diagnostic-accuracy statistics | 8–12 weeks |
| 1 | Medical imaging foundations | Image as array, color spaces, CLAHE, file formats (fundus, OCT, DICOM), perimetry tabular data | 4–6 weeks |
| 2 | Classical computer vision on ophthalmology data | Vessel/disc/cup segmentation, hand-crafted features, DRIVE/STARE/CHASE_DB1 | 4–6 weeks |
| 3 | Deep learning for ophthalmology | PyTorch, `timm`, MONAI, U-Net, transfer learning, RETFound | 8–12 weeks |
| 4 | Domain projects (the canon) | DR grading, OCT classification, glaucoma, multi-label disease, systemic-signal stretch; **electives**: biomedical NLP on ophthalmology text, ophthalmology genetics / bioinformatics | 12–16 weeks |
| 5 | Clinical translation | TRIPOD-AI / CONSORT-AI / SPIRIT-AI, FDA-cleared device case studies, dataset shift, fairness, Indonesian regulation (BPOM, Kemenkes, PDP Law UU 27/2022) | 4–8 weeks |

Phase 0 reuses [`mds-curriculum`](https://github.com/balinesthesia/mds-curriculum) Tier 1 + Tier 2 (Basic R). Phases 1–5 are this repo's net-new contribution.

---

## Reading canon (tight by design)

The canon is deliberately small. Expanding it prematurely produces breadth without competence.

- Gulshan V. et al. *JAMA* 2016 — first large-scale DR deep learning study.
- Ting D.S.W. et al. *JAMA* 2017 — multi-ethnic external validation.
- De Fauw J. et al. *Nat Med* 2018 — OCT triage at scale (DeepMind/Moorfields).
- Poplin R. et al. *Nat Biomed Eng* 2018 — cardiovascular risk from fundus.
- Abràmoff M.D. et al. — IDx-DR clearance and validation papers.
- Kermany D.S. et al. *Cell* 2018 — OCT classification benchmark.
- Zhou Y. et al. *Nature* 2023 — RETFound retinal foundation model.

Reporting standards:

- Collins G.S. et al. — TRIPOD-AI / TRIPOD+AI (2024 update).
- Liu X. et al. — CONSORT-AI / SPIRIT-AI.

Full annotated bibliography lives in `references/` (to be populated; see `TODO.md`).

---

## Tool stack

- **Python ≥ 3.12** managed by `uv` (single tool for envs, lockfile, scripts).
- **PyTorch ≥ 2.x** with `timm` for transfer learning, `MONAI` for medical-imaging pipelines.
- **R ≥ 4.4** for biostatistics (Phase 0 only).
- **Quarto** for all written content; renders to HTML + PDF.
- **Git + GitHub** for version control and publishing.
- **Optional cloud GPU**: Colab, Kaggle, Lightning Studio, or any L4/A10 spot instance.

Not in scope (avoiding premature complexity): Rust, Docker/Kubernetes, MLOps platforms. Add when a concrete bottleneck demands them.

---

## Honest caveats

- **Ophthalmology AI is saturated.** Reproducing a DR classifier teaches you the pipeline but contributes nothing publishable. A research contribution requires either (a) a novel clinical question, (b) an under-represented population (Indonesian retinal data is genuinely scarce in public benchmarks), or (c) a deployment/workflow angle.
- **Public datasets are biased.** EyePACS, Messidor, APTOS, ODIR-5K — none are representative of Southeast Asian populations at scale. External validation on local data is non-negotiable for clinical translation.
- **Foundation models change the curve.** RETFound (2023) and subsequent models make ImageNet-pretrained baselines pedagogically valuable but practically obsolete for new projects. The curriculum reflects this in Phase 3.
- **Consider pairing with a mentor.** Mentored fellowship models (e.g., UCSD's program) rely heavily on a senior mentor for project framing, paper-club facilitation, and committee-level deployment exposure that a curriculum cannot replicate. If a mentor is reachable — locally, regionally, or via an OSS community such as MONAI or Hugging Face medical-imaging — pair early. If no mentor is reachable in your context (a common Indonesian / LMIC reality), the learner who completes this curriculum **becomes the next mentor** for the learner after them. This pay-it-forward pedagogy is borrowed directly from `mds-curriculum`: every graduating cohort produces the teaching cadre for the next. It is not a limitation; it is the path.

---

## Credentialing (optional)

This curriculum confers no degree or certificate. Learners who want formal credentialing alongside or after this path may consider:

- **Indonesian institutional**: postgraduate programs at Universitas Indonesia, Universitas Gadjah Mada, or Universitas Udayana — biostatistics, biomedical informatics, or public health tracks where available.
- **International online**: HarvardX HMX, Stanford's online clinical informatics offerings, Johns Hopkins online MS in Health Informatics or Data Science. Verify current availability and admission criteria; offerings change.
- **Professional clinical informatics**: ACGME-equivalent pathways exist primarily in the US. Indonesian/regional equivalents are emerging — track Kemenkes and PERHATI/PERDAMI digital health initiatives.

Credentialing is orthogonal to competence. This curriculum is designed to produce the latter; the former is a separate decision.

## How to use this repo

1. Read `ARCHITECTURE.md` to understand the design rationale.
2. Read `TODO.md` to see the build plan for the curriculum content itself.
3. Once content is published (≥ `v0.1.0`), follow `phases/00-foundation/` → `phases/05-translation/` in order.
4. Each phase contains: learning objectives, readings, exercises, a capstone, and an assessment rubric.

---

## Repository layout (planned)

```
ophth-ds-curriculum/
├── README.md                  ← you are here
├── ARCHITECTURE.md            ← curriculum design rationale
├── TODO.md                    ← atomic build plan, SemVer-milestoned
├── LICENSE                    ← TBD before any content commit
├── CONTRIBUTING.md            ← contribution + style guide
├── CODE_OF_CONDUCT.md         ← standard OSS CoC
├── CHANGELOG.md               ← SemVer changelog
├── .github/
│   └── workflows/             ← CI: markdownlint, link-check, Quarto render
├── _quarto.yml                ← Quarto project config
├── phases/
│   ├── 00-foundation/
│   ├── 01-imaging-foundations/
│   ├── 02-classical-cv/
│   ├── 03-deep-learning/
│   ├── 04-domain-projects/
│   └── 05-clinical-translation/
├── references/                ← annotated bibliography
├── datasets/                  ← dataset cards (no data, only metadata + access notes)
└── assessments/               ← rubrics + sample capstones
```

---

## Versioning

This curriculum follows [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR** — breaking changes to phase structure or prerequisites.
- **MINOR** — new phase content, new readings, new exercises.
- **PATCH** — corrections, typo fixes, link updates.

Milestone targets are defined in `TODO.md`.

---

## Licensing

**Not yet decided.** Per the project owner's standing rule, LICENSE is selected before any content is committed beyond the scaffold. Candidates under consideration:

- **CC BY 4.0** — standard for open educational content; permissive, attribution required.
- **CC BY-SA 4.0** — copyleft for educational content; derivatives must share-alike.
- **CC BY-NC 4.0** — non-commercial; complicates downstream institutional reuse.
- **Dual: CC BY 4.0 for prose + MIT/Apache-2.0 for any code snippets** — common for curriculum repos that mix narrative and runnable code.

Decision deferred to first content PR. See `TODO.md` task `T0.2`.

---

## Acknowledgments

- [`balinesthesia/mds-curriculum`](https://github.com/balinesthesia/mds-curriculum) — sibling curriculum for anesthesia/ICU; Phase 0 is shared.
- The ophthalmology AI community — for publishing benchmarks, datasets, and reporting standards openly.
- 
