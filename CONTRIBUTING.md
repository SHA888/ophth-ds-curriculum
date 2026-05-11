# Contributing to ophth-ds-curriculum

> Thank you for considering a contribution. This document covers style, commit conventions, PR checklist, SPDX header policy, and a lightweight DCO requirement.

---

## Table of contents

1. [License and SPDX headers](#license-and-spdx-headers)
2. [Developer Certificate of Origin (DCO)](#developer-certificate-of-origin-dco)
3. [Commit conventions](#commit-conventions)
4. [Pull‑request checklist](#pull-request-checklist)
5. [Style guide](#style-guide)
6. [How to propose structural changes](#how-to-propose-structural-changes)

---

## License and SPDX headers

This repository uses a **dual‑license** model:

- **Prose and curriculum content** (`.md`, `.qmd`, `.Rmd`, `.rst`, `.txt`) – **CC BY 4.0**
- **Software, code, and configuration** (`.py`, `.R`, `.js`, `.ts`, `.yml`, `.yaml`, `.json`, `.toml`, `.sh`, `Makefile`, `Dockerfile`, etc.) – **MIT**

**SPDX header policy – mandatory**

Every file **must** start with an `SPDX-License-Identifier` comment on the first line. Missing headers cause CI failure.

### Examples

#### Markdown / Quarto / R Markdown (prose)
```markdown
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
```

#### Python
```python
# SPDX-License-Identifier: MIT
```

#### R
```r
# SPDX-License-Identifier: MIT
```

#### YAML / JSON / TOML / Shell / Makefile
```yaml
# SPDX-License-Identifier: MIT
```

#### Mixed Quarto notebooks (`.qmd` with code cells)
Place the prose header at the top of the document; code cells inherit the MIT license by convention:
```markdown
<!-- SPDX-License-Identifier: CC-BY-4.0 AND MIT -->
```

**No fallback** – if a file lacks an SPDX header, the CI workflow will reject the PR.

---

## Developer Certificate of Origin (DCO)

We adopt the lightweight DCO to certify contributor intent. Every commit must include a `Signed-off-by:` line, which can be added automatically with `git commit -s`.

```
Signed-off-by: Your Name <you@example.com>
```

The DCO states that you have the right to submit the contribution under the project's license and that you agree to the terms of the dual‑license model.

---

## Commit conventions

We use **Conventional Commits** to generate changelogs automatically and keep history readable.

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Use when |
|------|----------|
| `feat` | New curriculum content, exercise, or reading |
| `fix` | Correction to existing content or code |
| `docs` | Pure documentation changes (README, ARCHITECTURE, etc.) |
| `style` | Formatting, whitespace, punctuation — no semantic change |
| `refactor` | Restructuring content or code without changing behavior |
| `test` | Adding or updating tests / rubrics / checklists |
| `chore` | Tooling, CI, dependencies, repo maintenance |
| `revert` | Reverting a previous commit |

### Scopes (common)

- `phase0`, `phase1`, `phase2`, `phase3`, `phase4`, `phase5`
- `ci` — GitHub Actions, linting, rendering workflows
- `repo` — governance files (LICENSE, CONTRIBUTING, etc.)
- `deps` — dependency updates

### Examples

```
feat(phase1): add DICOM tag reading exercise

Includes sample fundus DICOM and a checklist rubric.
```

```
docs(repo): update CONTRIBUTING with DCO and mandatory SPDX headers
```

```
fix(phase3): correct RETFound paper citation year

Zhou et al. 2023, not 2022.
```

---

## Pull‑request checklist

Before requesting review, confirm every item below. PRs that do not pass the checklist will be returned for revision.

- [ ] **SPDX header** present on every new file.
- [ ] **DCO sign‑off** present on all commits (`git log --show-signature`).
- [ ] **Conventional Commit** format used for the PR title and all commits.
- [ ] **Link check** passed locally (`lychee` or manual verification for added URLs).
- [ ] **Markdown lint** passed (`markdownlint-cli2`).
- [ ] **Quarto render** passed for any changed `.qmd` files.
- [ ] **Binary rubric** included for any new capstone or exercise.
- [ ] **Dataset card** included for any new dataset reference (provenance, license, access, schema).
- [ ] **CHANGELOG.md** updated under `## [Unreleased]` if the change is user‑facing.
- [ ] **ARCHITECTURE.md** updated if the change affects design principles, phase contracts, or assessment philosophy.

---

## Style guide

### Prose

- **American English** spelling.
- **Sentence case** for headings (`## This is a heading`, not `## This Is A Heading`).
- **Oxford comma** in lists.
- **One sentence per line** in source Markdown — this produces clean diffs.
- **Cite with DOI** where available; fallback to arXiv ID or PubMed ID.
- **Avoid vendor‑specific product names** unless necessary for loading data (e.g., "Heidelberg `.e2e`" is acceptable because it names a file format, not a product endorsement).

### Code

- **Python**: formatted with `ruff`, typed where practical, docstrings in Google style.
- **R**: formatted with `styler`, roxygen2‑style documentation for functions.
- **No secrets or PHI** in any commit. Use synthetic or public‑domain data only.
- **Reproducible environments**: add dependencies to `pyproject.toml` or `renv.lock`, not ad‑hoc `pip install` notes in prose.

### Datasets

Every dataset referenced in the curriculum must have a card in `datasets/` following the template introduced in `TODO.md` T1.3.5. The card must specify:

1. **Provenance** — who collected it, when, where.
2. **License** — terms of use, redistribution, commercial use.
3. **Access** — URL, registration requirements, expected lifetime.
4. **Schema** — file layout, column / tag semantics, ground‑truth format.

---

## How to propose structural changes

Structural changes (new phases, reordering phases, changing assessment philosophy) require an **architecture decision record (ADR)**. Open a PR that:

1. Adds a file to `adr/` named `NNNN-<short-title>.md`.
2. Uses the template:

```markdown
# ADR‑NNNN: Title

## Status
Proposed / Accepted / Rejected / Superseded by ADR‑NNNN

## Context
What problem are we solving?

## Decision
What are we doing?

## Consequences
What becomes easier or harder?
```

3. Updates `ARCHITECTURE.md` if the ADR is accepted.

Content‑only changes (new exercises, reading additions, typo fixes) do not require an ADR.

---

*We enforce the above via CI; missing SPDX headers or missing DCO sign‑offs cause the workflow to fail.*
