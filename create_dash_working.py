import requests

headers = {
    'X-Api-Key': '427edcfa79240fdcc51efbbae6009891',
    'Content-Type': 'application/json',
}

data = '{"dashboard":{"metadata":{"version":1},"title":"Django Widget","icon":"none","visibility":"all","editable":"editable_by_owner","filter":{"event_types":["Transaction"],"attributes":["appName"]},"widgets":[{"visualization":"billboard","account_id":1774846,"data":[{"nrql":"SELECT count(*) from Transaction since 30 minutes ago"}],"presentation":{"title":"Threshold Event Chart","notes":"null","threshold":{"red":18000000,"yellow":8000000}},"layout":{"width":1,"height":1,"row":1,"column":1}}]}}'

response = requests.post('https://api.newrelic.com/v2/dashboards.json', headers=headers, data=data)
print(response.status_code, response.reason)
print("Request sent")
