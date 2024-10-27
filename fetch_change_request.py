import requests

# ServiceNow credentials and instance URL
instance_url = 'https://your_instance.service-now.com/api/now/table/change_request'
user = 'your_username'
password = 'your_password'

# Set the headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Fetch change requests
response = requests.get(instance_url, auth=(user, password), headers=headers)

if response.status_code == 200:
    change_requests = response.json().get('result', [])
    for change_request in change_requests:
        print(f"Number: {change_request['number']}, Short Description: {change_request['short_description']}, State: {change_request['state']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
