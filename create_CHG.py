import requests
from datetime import datetime,timezone

sys_id= "b7ccb8921b881f50167a20a5604bcbbf"
url = "https://preprod.service-now.com"
username =""
password = ""

date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time in UTC:", date)
endpoint = f"/api/sn_chg_rest/change/standard/{sys_id}"

body= {
"cmdb_ci": "ldxx90app312",
"start_date": "2026-10-26 15:20:07",
"end_date": "2026-10-31 05:20:07", 
"assignment_group": ""
}
# response = requests.post(url + endpoint, auth=(username, password), json=body)
# result = response.json()
# print("change number:", result['result']['number']['value'])
# print("change sys_id:", result['result']['sys_id']['value'])
# print("change state:", result['result']['state'])
