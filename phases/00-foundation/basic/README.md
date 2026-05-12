# Basic Tier

**Duration:** 16 weeks  
**Language:** R  
**Goal:** Critical consumer + reproducible researcher

---

## Overview

The Basic tier transforms clinicians into reproducible researchers. Residents learn to read, critique, and reproduce the statistical methods they encounter in anesthesia literature.

By the end of this tier, residents will be able to:
- **Read** a published anesthesia paper and understand its statistical methods
- **Critique** study design, analysis choices, and clinical applicability
- **Reproduce** the main analyses using R code and present findings in a Quarto report
- **Apply** statistical thinking to their own clinical questions

---

## Learning Goals

### By Week 4: Foundations
- Understand reproducibility rationale and common failure modes (Retraction Watch)
- Navigate R, RStudio, Quarto, and GitHub fluently
- Structure data for analysis (tidy data principles)
- Identify and classify clinical data types

### By Week 8: Exploratory Analysis
- Describe distributions, detect outliers, assess shape and spread
- Create publication-quality visualizations with ggplot2
- Generate clinical Table 1 with tableone
- Understand effect sizes vs. p-values

### By Week 12: Comparative Methods
- Compare groups using appropriate tests (t-test, Mann-Whitney, chi-square)
- Calculate and interpret odds ratios with confidence intervals
- Build and interpret linear and logistic regression models
- Check model assumptions and understand limitations

### By Week 16: Advanced & Capstone
- Understand survival analysis concepts (KM curves, log-rank, hazard)
- Classify study designs and identify their limitations
- Complete capstone: reproduce and critique a published anesthesia paper

---

## Module Structure

Each week follows the pattern:
```
week-NN/
├── index.qmd          # Resident-facing module
├── facilitator.qmd    # Facilitator notes
└── data/              # Module dataset or pointer
```

### Modules (v0.3.0 draft in progress)

| Week | Topic | Dataset | Key Packages |
|------|-------|---------|--------------|
| 01 | Environment & Philosophy | — | — |
| 02 | R + Quarto + GitHub | — | tidyverse |
| 03 | Data Structures | propofol-doses | dplyr, tibble |
| 04 | Clinical Data Types | propofol-doses | — |
| 05 | EDA I: Distributions | propofol-doses | ggplot2 |
| 06 | EDA II: Visualization | iop-map | ggplot2, lubridate |
| 07 | Table 1 | icu-outcomes | tableone |
| 08 | Inference Philosophy | icu-outcomes | — |
| 09 | Comparing Groups | icu-outcomes | stats, coin |
| 10 | Categorical Outcomes | icu-outcomes | stats, epitools |
| 11 | Linear Regression | icu-outcomes | stats, broom |
| 12 | Logistic Regression | icu-outcomes | stats, broom |
| 13 | Survival Basics | icu-outcomes | survival, survminer |
| 14 | Study Design | — | — |
| 15 | Capstone Workshop | — | — |
| 16 | Capstone Submission | — | — |

---

## Capstone

**Deliverable:** Quarto report reproducing and critiquing a published anesthesia paper + R code on GitHub.

**Requirements:**
- Select a paper from a target journal (Anesthesia & Analgesia, British Journal of Anaesthesia, Anesthesiology)
- Reproduce the main analysis (Table 1, key figures, primary outcome)
- Critique: study design, analysis choices, missing data handling, clinical applicability
- Submit: rendered HTML/PDF + GitHub repository with all code

**Template:** `basic/capstone/template.qmd` (to be authored)
**Rubric:** See `facilitator-guide` repo (to be authored)

---

## Datasets

### Basic Tier Datasets

Located in `../datasets/basic/`:

| Dataset | Rows | Variables | Description |
|---------|------|-----------|-------------|
| `propofol-doses.csv` | ~500 | id, weight_kg, dose_mg, case_duration, asa | Synthetic propofol induction doses with clinical covariates |
| `iop-map.csv` | ~10,000 | id, time_min, map, event | Intraoperative MAP time series, 10+ cases with event markers |
| `icu-outcomes.csv` | ~200 | id, age, sofa, apache, mortality_30d, los_icu | ICU admission variables with 30-day mortality outcome |

**Data Policy:** All datasets are synthetic or fully anonymized. No protected health information included. Generated for educational purposes only.

**Status:** Datasets listed are planned. See `../datasets/basic/README.md` for curation status.

---

## Prerequisites

Before starting Basic tier, residents must complete environment setup:

- R (4.3.0+)
- RStudio Desktop
- Quarto (1.4.0+)
- Git + GitHub account with SSH
- Essential packages: tidyverse, tableone, survival, survminer

**Setup Guide:** `../facilitator/setup-guide.qmd`  
**Verification Checklist:** `../facilitator/verification-checklist.qmd`

---

*See main [README.md](../README.md) for full curriculum overview.*
