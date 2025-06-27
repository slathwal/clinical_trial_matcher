# this file is used to download clinical trials data from clinicaltrials.gov.
# We will use the API from clinicaltrials.gov to download the data.

import requests
import pandas as pd

# Gynecological conditions to query
conditions = ["adenomyosis", "endometriosis", "PCOS", "uterine fibroids"]

fields = [
    "NCTId",
    "BriefTitle",
    "Condition",
    "EligibilityCriteria",
    "LocationCountry",
    "LocationState",
    "StudyType",
    "InterventionType",
    "OverallStatus",
    "HasResults"
]

all_trials = []
for condition in conditions:
    base_url = "https://clinicaltrials.gov/api/v2"
    endpoint = "/studies?"
    query = f"query.cond={condition}"
    filter = "&filter.overallStatus=NOT_YET_RECRUITING,RECRUITING,ACTIVE_NOT_RECRUITING,ENROLLING_BY_INVITATION"
    return_fields = f"&fields={','.join(fields)}"
    study_count = "&countTotal=true"
    page_size = "&pageSize=100"

    url = base_url + endpoint + query+filter+return_fields+study_count+page_size
    #print(url)

    response = requests.get(url)
    print(f"Total trial for {condition}:",response.json()["totalCount"])
    data = response.json()["studies"]
    for entry in data:
        all_trials.append(entry)

    # If number of trials is more than 100, then we need to fetch more trials from next page
    # We will check if nextPageToken key is present
    while "nextPageToken" in response.json().keys():
        next_page_token = response.json()["nextPageToken"]
        page_token ="&pageToken="+next_page_token 
        new_url = base_url + endpoint + query+filter+return_fields+study_count+page_size+page_token
        response = requests.get(new_url)
        #print(f"Condition: {condition}")
        if response.status_code == 200:
            data = response.json()["studies"]
            #print(response.json()["nextPageToken"])
            for entry in data:
                all_trials.append(entry)


# Collect the fields into a list of dictionaries for dataframe
output_fields = []
for trial in all_trials:
    trial_dict = {}
    for field in fields:
        #print(field)
        if field == "NCTId" :
            trial_dict[field] = trial["protocolSection"]["identificationModule"]["nctId"]
        if field == "BriefTitle":
            trial_dict[field] = trial["protocolSection"]["identificationModule"]["briefTitle"]
        if field == "Condition":
            trial_dict[field] = trial["protocolSection"]["conditionsModule"]["conditions"]
        if field == "EligibilityCriteria":
            trial_dict[field] = trial["protocolSection"]["eligibilityModule"]["eligibilityCriteria"]
        if field == "LocationCountry":
            if "contactsLocationsModule" in trial["protocolSection"]:
                if "locations" in trial["protocolSection"]["contactsLocationsModule"]:
                    locations_list = []
                    for location in trial["protocolSection"]["contactsLocationsModule"]["locations"]:
                        if "state" in location.keys():
                            locations_list.append(location["state"]+", "+location["country"])
                        else: 
                            locations_list.append(location["country"])   
                    trial_dict["Location"] = locations_list 
        #if field == "Phase":
            # A lot of trials do not have the phases key
        #    trial_dict[field] = trial["protocolSection"]["designModule"]["phases"]
        if field == "StudyType":
            trial_dict[field] = trial["protocolSection"]["designModule"]["studyType"]
        if field == "InterventionType":
            if "armsInterventionModule" in trial["protocolSection"]:
                trial_dict[field] = trial["protocolSection"]["armsInterventionModule"]["interventions"]
        if field == "OverallStatus":
            trial_dict[field] = trial["protocolSection"]["statusModule"]["overallStatus"]
        if field == "HasResults":
            trial_dict[field] = trial["hasResults"]
        

    output_fields.append(trial_dict)

# Save to DataFrame
df = pd.DataFrame(output_fields)

# Save CSV
# I am running the file from the  main folder. Therefore, the path has to be relative to the main folder as well
# The path will not be relative to the folder where file is present, but relative to the main folder.
df.to_csv("./data/clinical_trials_gyn.csv", index=False)

print("Saved trials to data/clinical_trials_gyn.csv")
