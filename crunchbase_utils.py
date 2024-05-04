import requests
import json
import os


#crunchbase_cookie = "cb_analytics_consent=granted; cid=Cig2ZmYluB0MUAAbLB85Ag==; featureFlagOverride=%7B%7D; featureFlagOverrideCrossSite=%7B%7D; _pxvid=92f937b4-0044-11ef-827e-8d843f6d2187; xsrf_token=MBu2v9YsYLm3+J1cXcRZsNTtkJKLP72bOhECuYm058M; __cflb=0H28vxzrpPtLNGTtMLYsEoPKg646GJ3qQ8deeo21ceg; pxcts=06501474-044b-11ef-8b13-3702b7f10d58; _pxhd=ma27yrbdpabY4jUPEXWoLox9wV4-ImXoN48Y-exnbqB62p7YdV4lCoj6TyCrb0nE7AvKlpzpVQ0gqY404XDT0w; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIwNjM4NDE1MC0yZTI0LTQ1NDYtYmQzZS1mYTM2NmRiNmQzNGUiLCJpc3MiOiJ1c2Vyc2VydmljZV81N2QwN2FlZV83MjIiLCJzdWIiOiI4NGQ2ZGMyZS0zMzhjLTQyMTYtOGIxMC1jOGNiMzZhODcxMWMiLCJleHAiOjE3MTQxOTk0MzIsImlhdCI6MTcxNDE5OTEzMiwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVEcEF3K0NZT3Z6NWk5MEQwRXM3SEdSUDNUTURvdUhGeE05MllNaUFrL1Q1TUw5b2IrOE9vWGlCL3lZY1BuZXlyVUVFOG9CNE15WjJ2eENvRG1uWndrRExRNUR4ZTRUamEyYmp1aGREUXZwZUN3aCtDT0krSVNPYjFjSVFlTTU2SThsUXRua25KS1VPbm9kWGJEaHc1QUlUajRvSVNTS1FyRHlsVk12cjJYdmNMYXF6M2ZDa0NNV2xQSkZrRVhPQmoxNTlkNnNxMzBqaVFVMTZURHpFeERCajBYa3RjS3FDS2czVEVhMDZKcFNsQUFmU0lqaUtWRDRybXllaWRoTGM5ci9IVncwMnVXdmlTQ1drQWFkMGhwOUR2VUNDSWlBQjI3OW9HZll3T1FLL2NVNGkxeFU3S1ZRaXpZNkJaTkNORkIwT3l2NWI3ZURuTk5FRk9LR0lJZ0JJQUdsekNsQjZqYzhDN3J3eWZtZklNNmgzdXNEWGJxRGoyUEk2K2pZSHJuSmFPWmJIbXprWGRvbys4ZjRXOEtOQWxucGtTOW4vcytFTmpUaFhVSmR4amtnTHRqY1U0UUxIWEQ4Vjd3Zkh3Y1hRaDdBcXh2VTBoS0Q0NjhlNVdhUkRKZ0ZzTFIxRlVmUUFVaWI5dTFZSVlQS2UwVDdmN1Ixb2F0UFd3M2JWUGdQcVlUa0NLZmU1Um9TWFdlSzkvejJBeGVJa3NvN3lkUEhxV3FTeVI1elJncHVJOGpBQkpDVFN0TERCcHlBdU9SM3BSN1VJeWZlenFPOG01QlRLRWtleDlGckljNlFncHFXbGl3bmdNdVVPTTlKaExWMTdHMmx6N01ueUNJM29NcldXeExTQk8wVy9YMU9jWDA5NXBBYlpOY0Q2cXNxTVBvcEVoaTlFN2llMG04Tzl6MHFaVGVvUE04L0NhU3FEYkd1aGVFWXRIbkE1N09pdE1CU0VMK25ROWE3NEhRZWNGd245YytMZmFBaUlyUERMeWpqaTdlaHBUZlh4ODljMUJrRzkraWlZRlo5NmVsTzRpRld3VUZMWHltWG10V3FubkFjdGNKaFRqZFVPQXlTNzRROVVTcCt4WHlNdkhjYjRmS3VuOVNLMm0zU2gzc2l6dTc4M1ZLQkxwVGxFSmtxeTlKZDcyWnM0SXZwcEx2ODB1T1h1d1g5eE43NEd0M2hMQ0VjaXlIbGRGQlIwMW1nN0pudU96U0RpMTI1c3dWb3k1VGZHaitZemtoRzN0VEZJbnFDWFFzcE01T0VXUm5HZEV0Nmk3RGowb2pkLzV3aHRXMk9RYU5sT1hJYWcrT1k0b3dIZDI5NG9GRmVPVCtVY1JneS9ueE52TEUveUpzUFFyeEl3M1ZCQUxkS1FTQ2M1MU1LdEx4SHJJajFwWi8yaWFOcGg4by9TREYyRDMwTmcxaG56TUNxZmVOVVRrVEtEeiIsInB1YmxpYyI6eyJzZXNzaW9uX2hhc2giOiItMTc4NTE2NDA0NCJ9fQ.ugG2hY6Py6sYkBHYYjZPEX7dwy9iIR-WRMU9X4L0alOeEhvOWyUQWt-v4F3waF-DiE7RcRV5OYKLUpt4ySwlgw; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+26+2024+23%3A27%3A25+GMT-0700+(Pacific+Daylight+Time)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ad905096-4e8a-4119-b261-a310e7e873d1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _px3=0994269b8b2108ef32548969b3b2f774d836bec26a4333ae359af0c2a4372541:dfwMQxV0o8SvBEVxSZ7hZNl1aReJxp2sd1RAUW13M5BltMO8vgNydSS3suT2eSfacx9J0zcsxJUg+ca91kGA+Q==:1000:XtqgqTCBSVlESwOIvusXkXM+IasWCnj+3/aas5IKL+d7s+mJX83LSeZduQuCfMq0Q6bspU6aGnH/z/9ETwXpU/DIAbtSCkC29thBj6ytvLg9JZIrLt1ezahsjghHfPa4CYie3yNZlQMa8rbGDTH+8ymnfBojvh9iGGAhoF9rSOoPOz06o3mDWQUFuzCUCVi0s7b2gQtwJVOsv/NGYFi7x9t/ejysy82YwcKD5+diPFo="
cookie_text = ""
try:
    with open("www.crunchbase.com.cookies.json") as f:
        crunchbase_cookie = json.load(f)
except FileNotFoundError:
    print("Please provide cookies in www.crunchbase.com.cookies.json")
    exit(1)
for cookie in crunchbase_cookie:
    this_cookie = f"{cookie['name']}={cookie['value']}; "
    cookie_text += this_cookie
print(cookie_text)


def get_job_title_by_company_uuid(company_uuid: str, keyword: str):
    cache_exist = os.path.exists(f"./crunchbase_cache/job_title/{company_uuid}-{keyword}.json")
    if cache_exist:
        with open(f"./crunchbase_cache/job_title/{company_uuid}-{keyword}.json") as f:
            print(f"Loading cache file: {company_uuid}-{keyword}.json")
            return json.load(f)

    url = f"https://www.crunchbase.com/v4/data/autocompletes?query={keyword}&collection_ids=job_title.org_has_contact_job_title.forward&parent_id={company_uuid}&limit=25"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.7",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers).json()
    with open(f"./crunchbase_cache/job_title/{company_uuid}-{keyword}.json", "w+") as f:
        json.dump(response, f, indent=4)
    return response


def get_people_by_job_title_uuid(company_uuid: str, job_title_uuid: str):
    cache_exist = os.path.exists(f"./crunchbase_cache/people/{company_uuid}-{job_title_uuid}.json")
    if cache_exist:
        with open(f"./crunchbase_cache/people/{company_uuid}-{job_title_uuid}.json") as f:
            print(f"Loading cache file: {company_uuid}-{job_title_uuid}.json")
            return json.load(f)
    url = "https://www.crunchbase.com/v4/data/searches/contacts?source=profile-contacts-card"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.7",
        "Content-Type": "application/json",
        "Cookie": cookie_text,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    body = {
      "collection_id": "contacts",
      "field_ids": [
        "name",
        "linkedin",
        "job_levels",
        "job_departments"
      ],
      "query": [
        {
          "type": "predicate",
          "field_id": "organization",
          "operator_id": "includes",
          "values": [company_uuid]
        },
        {
          "type": "predicate",
          "field_id": "num_contact_items",
          "operator_id": "gte",
          "values": [
            1
          ]
        },
        {
          "type": "predicate",
          "field_id": "job_titles",
          "operator_id": "includes",
          "values": [job_title_uuid]
        }
      ],
      "limit": 15,
      "order": [
        {
          "field_id": "job_priority",
          "sort": "desc"
        },
        {
          "field_id": "identifier",
          "sort": "asc"
        }
      ],
      "related_entities": [
        {
          "collection_id": "contact_item.has_contact_item.forward",
          "field_ids": [
            "job_title"
          ],
          "limit": 1
        }
      ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(body)).json()
    with open(f"./crunchbase_cache/people/{company_uuid}-{job_title_uuid}.json", "w+") as f:
        json.dump(response, f, indent=4)
    return response


def find_uuid_by_name(company_name):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.7",
        "Sec-Ch-Ua": r'"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    url = f"https://www.crunchbase.com/v4/data/autocompletes?query={company_name.replace(" ", "%20")}&collection_ids=organizations&limit=25&source=topSearch"
    content = requests.get(url, headers=headers)
    content = content.json()
    print(f"{company_name} has {len(content)} items")
    found_it = False
    for company in content["entities"]:
        found_it = True
        identify = company["identifier"]
        if identify["value"].lower() == company_name.lower() or identify["value"].lower() in company_name.lower():
            return identify["uuid"]


def add_to_list(company_id_list: list[str], list_id: str):
    if type(company_id_list) is str:
        company_id_list = [company_id_list]
    headers = {
        "path": f"/v4/md/lists/{list_id}/entity_ids",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.7",
        "Content-Type": "application/json",
        "Cookie": cookie_text,
        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    url = f"https://www.crunchbase.com/v4/md/lists/{list_id}/entity_ids"
    r = requests.post(url, headers=headers, json=company_id_list)
    print(f"Adding uuid {company_id_list}; status code: {r.status_code}; response: {r.text}")
