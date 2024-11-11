
import requests
from .config import BASE_URL, ENDPOINT

def get_infra_details(role=None, description=None):
    # Parameters for filtering
    params = {}
    if role:
        params["role"] = role
    if description:
        params["description"] = description

    try:
        # Send GET request to the FastAPI server
        response = requests.get(BASE_URL + ENDPOINT, params=params)
        
        # Raise an exception for any unsuccessful status codes
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Display the results
        print("Infra Details Retrieved:")
        for item in data:
            print(item)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
