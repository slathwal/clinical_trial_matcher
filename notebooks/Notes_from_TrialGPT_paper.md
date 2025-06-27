# Introduction
This document contains notes from the paper, [Matching patients to clinical trials with large language models](https://www.nature.com/articles/s41467-024-53081-z#Abs1)

The authors developed a tool called `TrialGPT`, available in a [github repository](https://github.com/ncbi-nlp/TrialGPT).

# Description from authors
TrialGPT is an end-to-end framework for zero-shot patient-to-trial matching with LLMs. TrialGPT consists of three modules:
1. Retrieval - large scale filtering to retrieve candidate trials
2. Matching - predicting criterion-level patient eligibility
3. Ranking - generating trial-level scores to rank the trials

The authors also performed evaluation of all three steps separately:
1. They achieved a recall of 90% relevant trials in the retrieval step.
2. They got an accuracy of 87.3% with explanations, close to expert performance for the matching step.
3. Ranking scores were correlated with human judgements and outperform best-competing models by 43.8% in ranking and excluding trials.
4. They also performed evaluation of time saved for experts with AI-assistance versus manually and found 42.6% time-saving for experts.

# Data used
- 183 synthetic patient notes are used
- Labeled data are available with over 75000 labels of trial eligibility for the 183 synthetic patients.

Data came from three main sources:
1. Special Interest Group on Information Retrieval (SIGIR) from 2016.
2. 2021 Clinical Trials (CT) Track of the Text REtrieval Conference (TREC).
3. 2022 Clinical Trials (CT) Track of the Text REtrieval Conference (TREC).

The SIGIR cohort has three eligibility labels:
- Irrelevant (“would not refer this patient for this clinical trial”)
- Potential (“would consider referring this patient to this clinical trial upon further investigation”)
- Eligible (“highly likely to refer this patient for this clinical trial”)

The TREC cohorts also have three eligibility labels:
- Irrelevant (“the patient is not relevant for the trial in any way”)
- Excluded/Ineligible (“the patient has the condition that the trial is targeting, but the exclusion criteria make the patient ineligible”)
- Eligible (“the patient is eligible to enroll in the trial”)

For the retrieval task, each dataset was used separately, i.e., only the combination of patient notes and trials included in each dataset were considered. 

# Notes on Cinical Trial Retrieval
- Given a patient note, locate hundreds of highly relevant candidate clinical trials from a large initial collection using `keyword-generation` and `hybrid-fusion retrieval`.
- A list of keywrods are generated based on patient summary.
- keywords are fed to a hybrid-fusion retriever (using both lexical and semantic information)
- The retrieval results from lexical matching and semantic matching are combined into a ranked list with reciprocal rank fusion.
- Lexical matching is done using BM25 and semantic matching is done using MedCPT.
- The authors also compared keyword based retrieval with retrieval directly from the raw note and found the keyword based retrieval to be much superior in performance.
- Recalls are plotted at different depths, where depth refers to the total number of trials retrieved.

# Notes on Clinical Trial Matching
- Matching predicts the criterion-level eligibility of each patient with three elements:
    - Natural language explanations showing relevance of the patient to the criterion
    - locations of relevant sentences in the patient note that are relevant to the target criterion
    - the eligibility classification indicating whether the patient meets a particular criterion.

# Notes on Clinical Trial Ranking
- Results from the matching step are aggregated at the level of each trial and scores are used to get a ranked list of trials based on the eligibility of a given patient.

# Questions
1. What is keyword-generation and hybrid-fusion retrieval used in the trial retrieval step?
LLMs are used to generate a list of keywords from the patient note for the initial screening of trials at scale. 
For each keyword, a hybrid retriever with both lexical matching and semantic matching is used to get a list of relevant clinical trials.

2. What is reciprocal rank fusion - the technique used to combine list of trials obtained in the first step using lexical information retrieval and semantic information retrieval?
- Mathematical definition of reciprocal rank fusion is provided in the methods section of the paper.

# Other/Miscellaneous thoughts
There are two main types of tasks in patient-trial matching:
1. `trial-to-patient` - matches one clinical trial to a list of candidate patients, which is what clinical trial organizers need.
2. `patient-to-trial` - matches one patient to a list of candidate clinical trials. The paper focuses on patient-to-trial matching where individual patients and doctor referral offices can get a list of candidate trials that they are potentially eligible for.

- A lot of papers on matching patients to clinical trials focus on data pre-processing such as extracting patient current history, past history, family history and structuring the inclusion and exclusion criteria of trials, with special pre-proicessing done to deal with negations. The interesting part about this work is that apart from key-word extractionfrom patient notes, this paper does not seem to have done any pre-processing on clinical trials. Neither have they focused on extracting inclusion and exclusion criteria and dealing with negations. It would be interesting to compare the effect of pre-processing on their pipeline.

- They have a deliberate focus on human-in-the-loop and report a metric on how their tool can help make human evaluators more efficient. They mention that their goal is not to automate the process completely, but to design a tool that can help human evaluators make better decisions. Their design choice of having the model outpt a reason for eligibility/ineligibility is also due to their philosophy of human-in-the-loop.

- They did not use geolocations and recruitment status of the clinical trials and only use the patient note and eligibility criteria of the trials.
- They have provided a detailed description of their methods and prompts that they used.