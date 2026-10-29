import requests
from datetime import datetime,timezone,timedelta

sys_id= "" #sys_id of CHG_no.
url = "https://instance.service-now.com"
username =""
password = ""
state= "scheduled"

date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time in UTC:", date)
endpoint = f"/api/sn_chg_rest/change/{sys_id}"

body= {
    
    "assignment_group": "",
    "state": state
}
response = requests.patch(url + endpoint, auth=(username, password), json=body)
result = response.json()
print("response:", result)
print("change number:", result['result']['number']['value'])
print("change sys_id:", result['result']['sys_id']['value'])
print("change state:", result['result']['state'])
