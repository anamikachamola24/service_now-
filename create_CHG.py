import requests,os 
from datetime import datetime,timezone,timedelta
import argparse

parser = argparse.ArgumentParser(description="Create a change request in ServiceNow")
parser.add_argument("--sys_id", default=os.environ.get("sys_id",     ""), required=not bool(os.environ.get("sys_id")), help="Sys ID of the CHG template")
parser.add_argument("--url", default=os.environ.get("url",     ""), required=not bool(os.environ.get("url")), help="ServiceNow instance URL")
parser.add_argument("--username", default=os.environ.get("username",     ""), required=not bool(os.environ.get("username")), help="ServiceNow username")
parser.add_argument("--password", default=os.environ.get("password",     ""), required=not bool(os.environ.get("password")), help="ServiceNow password")
parser.add_argument("--assignment_group", default=os.environ.get("assignment_group", ""), required=not bool(os.environ.get("assignment_group")), help="Assignment group")
parser.add_argument("--assigned_to", default=os.environ.get("assigned_to", ""), required=not bool(os.environ.get("assigned_to")), help="Assigned to")
parser.add_argument("--ci",default=os.environ.get("ci",     ""), required=not bool(os.environ.get("ci")), help="Configuration item")
parser.add_argument("--ritm", default=os.environ.get("ritm",     ""), required=False, help="RITM number")
parser.add_argument("--tenant_name", default=os.environ.get("tenant_name",     ""), required=False, help="Tenant name")
parser.add_argument("--vrf_name", default=os.environ.get("vrf_name",     ""), required=False, help="VRF name")
parser.add_argument("--bridge_domain_name", default=os.environ.get("bridge_domain_name",     ""), required=False, help="Bridge Domain name")
parser.add_argument("--epg_name", default=os.environ.get("epg_name",     ""), required=False, help="EPG name")
parser.add_argument("--vlan_id", default=os.environ.get("vlan_id",     ""), required=False, help="VLAN ID")
parser.add_argument("--network_subnet", default=os.environ.get("network_subnet",     ""), required=False, help="Network/Subnet (CIDR)")
parser.add_argument("--gateway_ip", default=os.environ.get("gateway_ip",     ""), required=False, help="Gateway IP")
parser.add_argument("--physical_domain", default=os.environ.get("physical_domain",     ""), required=False, help="Physical Domain")
args = parser.parse_args()

sys_id = args.sys_id #sys_id of CHG_template
url = args.url
username = args.username
password = args.password
assignment_group = args.assignment_group # Replace with the actual assignment group
assigned_to = args.assigned_to # Replace with the actual assigned to
ci = args.ci # Replace with the actual CI

ritm = args.ritm  # Replace with the actual RITM number
tenant_name = args.tenant_name  # Replace with the actual tenant name
vrf_name = args.vrf_name  # Replace with the actual VRF name
bridge_domain_name = args.bridge_domain_name  # Replace with the actual Bridge Domain name
epg_name = args.epg_name  # Replace with the actual EPG name
vlan_id = args.vlan_id  # Replace with the actual VLAN ID
network_subnet = args.network_subnet  # Replace with the actual Network/Subnet (CIDR)
gateway_ip = args.gateway_ip  # Replace with the actual Gateway IP
physical_domain = args.physical_domain  # Replace with the actual Physical Domain

current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
end_date = (datetime.now(timezone.utc) + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time in UTC:", current_date)
endpoint = f"/api/sn_chg_rest/change/standard/{sys_id}"

body= {
    "cmdb_ci": ci,
    "start_date": current_date,
    "end_date": end_date, 
    "assignment_group": assignment_group,
    "assigned_to": assigned_to  
}
if sys_id == "b7ccb8921b881f50167a20a5604bcbbf":
    body["description"] = f"Please update the following \n\
    Is a snapshot/backout configuration captured before the change?  Yes / No\n\
    RITM #: {ritm}\n\
    Tenant Name: {tenant_name}\n\
    VRF Name: {vrf_name}\n\
    Bridge Domain Name: {bridge_domain_name} \n\
    EPG Name: {epg_name}\n\
    VLAN ID: {vlan_id}\n\
    Network/Subnet (CIDR): {network_subnet}\n\
    Gateway IP: {gateway_ip}\n\
    Physical Domain: {physical_domain}\n"
try:
    response = requests.post(url + endpoint, auth=(username, password), json=body)
    result = response.json()
    print("change number:", result['result']['number']['value'])
    print("change sys_id:", result['result']['sys_id']['value'])
    print("change state:", result['result']['state'])
except Exception as e:
    print("response:", response.json())
    print("Error occurred while creating change:", e)
