import requests
import time
import json
from collections import deque
# URL for the Pinnacle Odds API
url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/details"

# Query parameters, including the specific event_id you want to fetch details for
querystring = {"event_id": "1603976105"}

# Headers containing your RapidAPI key and the API host
headers = {
    "x-rapidapi-key": "bdc3d7bd21msh6bab73819d2bf38p13a880jsn2c5acc778970",  # Replace with your actual RapidAPI key
    "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}
last_10_differences = deque(maxlen=10)
# Loop to make the API call every 10 seconds
while True:
    # Make the GET request to the API
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        print(f" {data}")
        
    else:
        print(f"Failed to fetch data: {response.status_code}")
    
    # Wait for 10 seconds before making the next API call
   
