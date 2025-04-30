Note: This repository is a work in progress and not fully functional yet.


# 🧬 Clinical Trial Matcher for Rare Disease Patients

This project extracts and structures eligibility and disease info from clinical trial text using NLP and matches it to rare disease patients' phenotypes (HPO terms). It recommends the most relevant clinical trials for a given patient profile.

## 🚀 Features
- Text extraction from clinical trial descriptions
- Semantic similarity scoring between trials and patient phenotypes
- Optional UI using Streamlit

## 🛠️ Tech Stack
- Python, spaCy, Pandas
- HPO term matching
- ClinicalTrials.gov API

## 🗂️ Folder Structure
- `data/` – sample input data (clinical trials + patient phenotypes)
- `src/` – all core matching and NLP logic
- `notebooks/` – step-by-step development in Jupyter
- `app/` – demo app with Streamlit

## 📦 Installation
```bash
git clone https://github.com/your-username/clinical-trial-matcher.git
cd clinical-trial-matcher
pip install -r requirements.txt