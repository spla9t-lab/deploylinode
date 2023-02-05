import requests
import json
import time


# Replace your_api_key_here with your actual Linode API key, and 
# Replace your_root_password with the desired root password for your new Linode. 
# 
# You can adjust the time.sleep(30) line to specify how long you want to wait 
# before checking the status of the deployed Linode.

# Writen by ChatGPT and Blake Ruecker



# Set the Linode API key
api_key = "your_api_key_here"

# Set the headers for the API request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# Define the endpoint to create a new Linode
endpoint = "https://api.linode.com/v4/linode/instances"

# Set the data for the API request
data = {
    "type": "g6-nanode-1",
    "region": "us-west",
    "image": "linode/ubuntu22.04",
    "root_pass": "your_root_password",
    "label": "my_first_linode_vm",
}

# Make a POST request to the Linode API to create a new Linode
response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Check the status code of the response
if response.status_code == 200:
    # Parse the response as JSON
    data = json.loads(response.text)

    # Get the ID of the newly created Linode
    linode_id = data["id"]

    # Print a message indicating that the Linode has been created
    print(f"Linode ID {linode_id} has been created.")
else:
    # Print an error message
    print(f"Failed to create Linode. Status code: {response.status_code}")
    print(f"Response: {response.text}")

# Wait for a specified amount of time
time.sleep(30)

# Define the endpoint to retrieve the Linode details
endpoint = f"https://api.linode.com/v4/linode/instances/{linode_id}"

# Make a GET request to the Linode API
response = requests.get(endpoint, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # Parse the response as JSON
    data = json.loads(response.text)

    # Get the status of the Linode
    linode_status = data["status"]

    # Print the status
    print(f"Linode ID {linode_id} is in the '{linode_status}' state.")
else:
    # Print an error message
    print(f"Request failed with status code {response.status_code}.")
