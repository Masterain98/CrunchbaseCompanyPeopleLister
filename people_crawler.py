import json
from crunchbase_utils import get_people_by_job_title_uuid, get_job_title_by_company_uuid, find_uuid_by_name, add_to_list
import pandas as pd
import os
from urllib.parse import urlparse


SAAS_LIST_UUID = "c32d706a-7bad-427c-8cbf-e8017e963ad5"
KEYWORD_LIST = ["CEO", "CMO", "CTO"]
LINKEDIN_URL = "https://www.linkedin.com/in/{linkedin_id}/"

#file_name = "nvidia_exhibitors_v3.xlsx"  # CHANGE THIS
directory = './raw'


def name_process(name: str) -> list:
    if not name or name.strip() == "":
        return ["", "", ""]
    name = name.split(" ")
    match len(name):
        case 0:
            fn = ""
            mn = ""
            ln = ""
        case 1:
            fn = name[0]
            mn = ""
            ln = ""
        case 2:
            fn = name[0]
            mn = ""
            ln = name[1]
        case 3:
            fn = name[0]
            mn = name[1]
            ln = name[2]
        case _:
            fn = name[0]
            mn = name[1]
            ln = ""
            for i in range(2, len(name)):
                ln += name[i] + " "
            ln = ln[:-1]
    return [fn, mn, ln]


if __name__ == "__main__":
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_type = ".csv"
        elif file_name.endswith(".xlsx"):
            file_type = ".xlsx"
        else:
            raise RuntimeError("Unsupported file type")

        if file_type == ".csv":
            df = pd.read_csv(f"./raw/{file_name}")
        elif file_type == ".xlsx":
            df = pd.read_excel(f"./raw/{file_name}", sheet_name="Sheet1")
        else:
            raise RuntimeError("Unsupported file type")
        if os.path.exists(f"./raw/{file_name.replace(file_type, "")}.json"):
            with open(f"./raw/{file_name.replace(file_type, "")}.json") as f:
                final_list = json.loads(f.read())
                company_json_list = list(tuple([c["Company"] for c in final_list]))
        else:
            final_list = []
            company_json_list = []

        for i, r in df.iterrows():
            print(f"Processing index of {i}")
            company_name = r["Organization Name"]
            if company_name in company_json_list:
                print(f"Skipping {company_name}")
                continue
            company_uuid = find_uuid_by_name(company_name)
            if company_uuid is None:
                print(f"Skipping {company_name} as no UUID")
                continue
            url = r["Website"]
            for keyword in KEYWORD_LIST:
                try:
                    job_title_response = get_job_title_by_company_uuid(company_uuid, keyword)
                    job_title_list = job_title_response["entities"]
                except KeyError as e:
                    print(job_title_response)
                    os.remove(f"./crunchbase_cache/job_title/{company_uuid}-{keyword}.json")
                    raise RuntimeError(f"Error: {e}\nCompany: {company_name} ({company_uuid})")
                for job_title in job_title_list:
                    job_title = job_title["identifier"]
                    job_title_name = job_title["value"]
                    job_title_uuid = job_title["uuid"]
                    if keyword.lower() not in job_title_name.lower():
                        continue

                    # get people
                    try:
                        print(
                            f"Processing {company_name} ({company_uuid}) -> Job title: {job_title_name} ({job_title_uuid})")
                        people_list_result = get_people_by_job_title_uuid(company_uuid, job_title_uuid)
                        people_list = people_list_result["entities"]
                    except (TypeError, KeyError) as e:
                        print(people_list_result)
                        os.remove(f"./crunchbase_cache/people/{company_uuid}-{job_title_uuid}.json")
                        raise RuntimeError(
                            f"Error: {e}\nCompany: {company_name} ({company_uuid})\nJob title: {job_title_name} ({job_title_uuid})")
                    for this_person in people_list:
                        this_person_property = this_person["properties"]
                        this_person_name = this_person_property["name"]
                        if "linkedin" in this_person_property:
                            this_person_linkedin = LINKEDIN_URL.format(linkedin_id=this_person_property["linkedin"])
                        else:
                            this_person_linkedin = ""
                        this_person_job_title = \
                            this_person["related_entities"]["contact_item.has_contact_item.forward"]["entities"][0][
                                "properties"]["job_title"]

                        name_process_result = name_process(this_person_name)

                        this_person_dict = {
                            "Company": company_name,
                            "URL": url,
                            "Domain": urlparse(url).netloc,
                            "Job Title": job_title_name,
                            "Person Name": this_person_name,
                            "First Name": name_process_result[0],
                            "Middle Name": name_process_result[1],
                            "Last Name": name_process_result[2],
                            "Linkedin": this_person_linkedin,
                            "Person Job Title": this_person_job_title
                        }
                        final_list.append(this_person_dict)
                        with open(f"./output/{file_name.replace(file_type, "")}.json", "w+") as f:
                            json.dump(final_list, f, indent=4)
        with open(f"./output/{file_name.replace(file_type, "")}.json") as f:
            final_list = json.load(f)
            print(f"Total: {len(final_list)}")

        final_list = [dict(t) for t in {tuple(d.items()) for d in final_list}]
        print(f"Total after removing duplicates: {len(final_list)}")
        df = pd.DataFrame(final_list)
        df.to_excel(f"./output/{file_name.replace(file_type, "")}.updated.xlsx", index=False)
