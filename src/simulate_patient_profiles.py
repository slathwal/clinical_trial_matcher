import pandas as pd

# Simulated patient data
data = [
    {
        "patient_id": "P001",
        "diagnosis": "Endometriosis",
        "hpo_terms": "HP:0000132 (Menorrhagia); HP:0034267 (Pelvic pain); HP:0000789 (Infertility); HP:0012378 (Fatigue)"
    },
    {
        "patient_id": "P002",
        "diagnosis": "PCOS",
        "hpo_terms": "HP:0000141 (Amenorrhea); HP:0001513 (Obesity); HP:0001007 (Hirsutism); HP:0000855 (Insulin resistance)"
    },
    {
        "patient_id": "P003",
        "diagnosis": "Adenomyosis",
        "hpo_terms": "HP:0034267 (Pelvic pain); HP:0100608 (Metrorrhagia); HP:0100607 (Dysmenorrhea); HHP:0012378 (Fatigue)"
    },
    {
        "patient_id": "P004",
        "diagnosis": "Uterine Fibroids",
        "hpo_terms": "HP:0034267 (Pelvic pain); HP:0100608 (Abnormal uterus bleeding); HP:0000012 (Urinary urgency); HP:0001903 (Anemia)"
    },
    {
        "patient_id": "P005",
        "diagnosis": "PCOS",
        "hpo_terms": "HP:0000141 (Amenorrhea); HP:0001061 (Acne); HP:0001513 (Obesity); HP:0001007 (Hirsutism); HP:0100608 (Abnormal uterus bleeding)"
    },
]


# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/sample_patients_hpo.csv", index=False)

print("Saved patient phenotype data to data/sample_patients_hpo.csv")
