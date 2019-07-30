import requests
import os
from json_data import apm_dashboard

# Get API and account ID info
api_key = os.environ.get("API_KEY")
rpm_account_id = os.environ.get("ACCOUNT_ID")

# Insert api key to headers
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json',
}
# Assign variable to apm_dashboard
dashboard = apm_dashboard
# Insert rpm account id
data = dashboard.replace("rpm_account_id", rpm_account_id)

# Send resquest
response = requests.post(
    'https://api.newrelic.com/v2/dashboards.json', headers=headers, data=data)
print(response.status_code, response.reason)
print("Request sent, your dashboard is ready to view.")
