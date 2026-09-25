import json

import requests

# Get markets
#markets =requests.get("https://gamma-api.polymarket.com/events?start_date_min=2024-07-09T00:00:00Z")
markets = requests.get("https://gamma-api.polymarket.com/events?slug=nba-nyk-lal-2025-03-06")
#markets = requests.get("https://gamma-api.polymarket.com/events?tag=nfl")

#markets = requests.get("https://gamma-api.polymarket.com/events/17603")
print(markets.json())

# Get events
events = requests.get("https://gamma-api.polymarket.com/events?start_date_min=2025-00-01T00:00:00Z")
json_data = json.dumps(events.json(), indent=4)
with open("events.json", "w") as file:
    file.write(json_data)
print(
    "Data formatted and saved to events.json, look for clobTokenIds later in this tutorial"
)


#nba-cle-det-2025-02-05