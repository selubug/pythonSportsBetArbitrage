import requests
import time
from collections import deque
from py_clob_client.client import ClobClient
from py_clob_client.client import ApiCreds
from py_clob_client.clob_types import OrderArgs
from py_clob_client.order_builder.constants import BUY
from py_clob_client.order_builder.constants import SELL
from py_clob_client.clob_types import MarketOrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY
import os
from telegram import Bot
import asyncio
# Setup for the Polymarket API (ClobClient)
host = "https://clob.polymarket.com"
private_key = "0xd29e629f6d71aacad6ee5b15f026de711451575db881d456b068c55e2b728a94"
chain_id = 137  # Polygon Mainnet
creds1 = ApiCreds(   
    api_key="122380e4-1720-ec43-ec56-5052b6fd7c41",
    api_secret="HRUfMWUnd20zs4A22hQDkrzPbWioHoZkHJlueCkKQaY=",
    api_passphrase="29fa091d5f74b9875b573e410e9554eb76624cc350b0bbe5340d625fff07e0a3",
)
bot_token = '7587403778:AAGDMdG_Yf8jn-pkZ3xtoZZ46hsyLsIf0CI'
chat_id = '7107063732'
bot = Bot(token=bot_token)
client = ClobClient(host, key=private_key, chain_id=chain_id, creds=creds1, signature_type=1, funder="0xf7777B2D3f6E9603486B6CEEBC2187E4666a34a5")
async def send_message():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text="BUY ORDER")

# Run the event loop
# Function to create and send orders
def place_orders_away():
    order_args1 = MarketOrderArgs(
        token_id="35148400527010834388818373307797963749475057799722035376117183256447544864560",
        amount=1.0,  # $$$
        side=BUY,
    )
   

    # Create and send the buy orders
    signed_order1 = client.create_market_order(order_args1)
   
    print(f"Placed Order 1: {signed_order1}")

    
    resp1 = client.post_order(signed_order1, OrderType.FOK)
    
    print(f"Order Response 1: {resp1}")
   
def place_orders_home():
   
    order_args3 = MarketOrderArgs(
        token_id="60935938813239991616950421871927241268329612745578806158829905952654621041892",
        amount=1.0,  # $$$
        side=BUY,
    )
   
    # Create and send the buy orders
   
    signed_order3 = client.create_market_order(order_args3)
   
    print(f"Placed Order 3: {signed_order3}")
    
   
    resp3 = client.post_order(signed_order3, OrderType.FOK)
    
    print(f"Order Response 3: {resp3}")
  
# URL for the Pinnacle Odds API
url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/details"
querystring = {"event_id": " 1604395774"}


# Headers containing your RapidAPI key and the API host
headers = {
    "x-rapidapi-key": "bdc3d7bd21msh6bab73819d2bf38p13a880jsn2c5acc778970",  # Replace with your actual RapidAPI key
    "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}

# Deque to store the last 10 differences
last_10_differences = deque(maxlen=10)

# Function to calculate implied probability from decimal odds
def calculate_implied_probability(decimal_odds):
    return 1 / decimal_odds

# Loop to make the API call every 10 seconds
while True:
    # Make the GET request to the API
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Navigate to the money line for the first event in the response
        if 'events' in data and len(data['events']) > 0:
         event = data['events'][0]  # Get the first event
         if 'money_line' in event['periods']['num_0']:
          money_line = event['periods']['num_0']['money_line']
          if money_line:
             home_moneyline = money_line['home']
             away_moneyline = money_line['away']
             print(f"Home Moneyline (Decimal): {home_moneyline}, Away Moneyline (Decimal): {away_moneyline}")
                    
           
            
                  # Print the relevant data (Home Moneyline)
             print("Home Moneyline (Decimal):", home_moneyline)
           
             # Calculate the implied probability for the current home moneyline
             implied_probability = calculate_implied_probability(home_moneyline)
             print(f"Implied Probability for Current Moneyline: {implied_probability * 100}%")

             # Calculate the difference and append to the deque
             difference = abs(home_moneyline)
             last_10_differences.append(difference)
             print(f"Moneyline Difference: {difference}")

             if len(last_10_differences) > 1:
                # Get the previous stored decimal odds value
                last_decimal_odds = last_10_differences[-2]
                
                # Calculate the implied probability for the previous decimal odds
                last_implied_probability = calculate_implied_probability(last_decimal_odds)
                
                # Calculate the change in implied probability
                implied_odds_change = (implied_probability - last_implied_probability) * 100
                print(f"Implied Probability Change: {implied_odds_change}%")

                # Check if the change is significant enough to place orders
                if implied_odds_change > 0 and abs(implied_odds_change) > 8  and abs(implied_odds_change) <= 10:
                    print("The team's chances have improved (higher probability of winning), and the implied probability change is more than 5%, placing orders.")
                    place_orders_home()
                    asyncio.run(send_message())
                if implied_odds_change < 0 and abs(implied_odds_change) > 8 and abs(implied_odds_change) <= 10:
                    print("The team's chances have decreased (lower probability of winning), and the implied probability change is more than 5%, placing orders.")
                    place_orders_away()
                    asyncio.run(send_message())
                if implied_odds_change > 0 and abs(implied_odds_change) > 10:
                    print("The team's chances have improved (higher probability of winning), and the implied probability change is more than 10%, placing orders.")
                    place_orders_home()
                    asyncio.run(send_message())
                if implied_odds_change < 0 and abs(implied_odds_change) > 10:
                    print("The team's chances have decreased (lower probability of winning), and the implied probability change is more than 10%, placing orders.")
                    place_orders_away()
                    asyncio.run(send_message())
          else:
                    print("No moneyline available.")
                    # If no moneyline, check which team won
                    team_1_score = event['period_results'][0]['team_1_score']
                    team_2_score = event['period_results'][0]['team_2_score']

                    if team_1_score > team_2_score:
                        print(f"{event['home']} won the game!")
                        place_orders_home()
                        asyncio.run(send_message())
                        break
                    elif team_1_score < team_2_score:
                        place_orders_away()
                        print(f"{event['away']} won the game!")
                        asyncio.run(send_message())
                        break
                    else:
                        print("The game is a draw.")
         else:
                print("Moneyline is not available for this event.")
        else:
            print("No events data available.")
    else:
        print(f"Failed to fetch data: {response.status_code}")
    