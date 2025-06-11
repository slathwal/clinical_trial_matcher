Note: This repository is a work in progress and not fully functional yet. The problem of trying to match patient profiles to the inclusion and exclusion criteria has sent me on a tangent to learn about word embeddings and more in NLP. I am focusing on learning some of the fundamentals of NLP in the [neural networks repostory](https://github.com/slathwal/neural_networks) and will come back to this project once I am comfortable with the NLP fundamentals.


# Clinical Trial Matcher for Gynaecological Disease

This project is aimed at matching patients with the most relevant ongoing clinical trials. The goal is to extract eligibility criteria and disease information from clinical trial text, and patient clinical history, and produce a ranked list of clinical trials that the patient is eligible for

## Features
- Text extraction from clinical trial descriptions and patient profiles
- Similarity scoring between trials and patient profiles
- Optional UI using Streamlit

## Tech Stack
- Python
- ClinicalTrials.gov API
- ...

## Folder Structure
- `data/` – sample input data (clinical trials + patient clinical profiles)
- `src/` – all scripts as .py files
- `notebooks/` – step-by-step development of different parts in Quarto documents
- `app/` – demo app with Streamlit

## Installation
```bash
git clone https://github.com/slathwal/clinical-trial-matcher.git
cd clinical-trial-matcher
conda env create -f clinical_trial.yml
