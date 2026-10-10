import requests
import time
import aiohttp
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
private_key = ""
chain_id = 137  # Polygon Mainnet
creds1 = ApiCreds(   
    api_key="",
    api_secret="",
    api_passphrase="",
)
bot_token = '7'
chat_id = '7107063732'
bot = Bot(token=bot_token)
client = ClobClient(host, key=private_key, chain_id=chain_id, creds=creds1, signature_type=1, funder="0xf7777B2D3f6E9603486B6CEEBC2187E4666a34a5")
async def send_message():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text="BUY ORDER")

#raptors

def place_order_sync(order_args):
    signed_order = client.create_order(order_args)
    print(f"Placed Order: {signed_order}")
    resp = client.post_order(signed_order, OrderType.GTD)
    print(f"Order Response: {resp}")
    return resp
def place_order_syncMarket(order_args):
    signed_order = client.create_market_order(order_args)
    print(f"Placed Order: {signed_order}")
    resp = client.post_order(signed_order, OrderType.FOK)
    print(f"Order Response: {resp}")
    return resp
async def place_order_async(order_args):
    response = await asyncio.to_thread(place_order_sync, order_args)
    return response
async def place_order_asyncMarket(order_args):
    response = await asyncio.to_thread(place_order_syncMarket, order_args)
    return response

order_args2 = MarketOrderArgs(
        token_id="4332083293447018793173941939865251019911946428389167077735301343836436715572",
        amount=5.0,  # $$$
        side=BUY,)
order_args3 = MarketOrderArgs(
        token_id="23263316335447548230851891669242583608504473671920087737283656839073393980364",
        amount=5.0,  # $$$
        side=BUY,)
order_args4 = MarketOrderArgs(
        token_id="8215640582137371720166104413852463856055298514314421989383820721065174535220",
        amount=5.0,  # $$$
        side=BUY,)
order_args5 = MarketOrderArgs(
        token_id="9837790504602694498213154818257188376289930051849077202229379591346799845527",
        amount=5.0,  # $$$
        side=BUY,)
order_args6 = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=5.0,  # $$$
        side=BUY,)
order_args7 = MarketOrderArgs(
        token_id="113121914141598676314954132698127812234826431368664164098105680898541149647625",
        amount=5.0,  # $$$
        side=BUY,)
order_args8 = MarketOrderArgs(
        token_id="100724911876216248060147087477446952370038118754796328030159980241674397597586",
        amount=5.0,  # $$$
        side=BUY,)
order_args9 = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=5.0,  # $$$
        side=BUY,)
order_args10 = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=5.0,  # $$$
        side=BUY,)

order_args2a = MarketOrderArgs(
        token_id="4332083293447018793173941939865251019911946428389167077735301343836436715572",
        amount=3.0,  # $$$
        side=SELL,)
order_args3a = MarketOrderArgs(
        token_id="23263316335447548230851891669242583608504473671920087737283656839073393980364",
        amount=3.0,  # $$$
        side=SELL,)
order_args4a = MarketOrderArgs(
        token_id="8215640582137371720166104413852463856055298514314421989383820721065174535220",
        amount=3.0,  # $$$
        side=SELL,)
order_args5a = MarketOrderArgs(
        token_id="9837790504602694498213154818257188376289930051849077202229379591346799845527",
        amount=3.0,  # $$$
        side=SELL,)
order_args6a = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=3.0,  # $$$
        side=SELL,)
order_args7a = MarketOrderArgs(
        token_id="113121914141598676314954132698127812234826431368664164098105680898541149647625",
        amount=3.0,  # $$$
        side=SELL,)
order_args8a = MarketOrderArgs(
        token_id="100724911876216248060147087477446952370038118754796328030159980241674397597586",
        amount=3.0,  # $$$
        side=SELL,)
order_args9a = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=3.0,  # $$$
        side=SELL,)
order_args10a = MarketOrderArgs(
        token_id="71698869454814263683698084644923527762610444752009417126704833083354026192168",
        amount=3.0,  # $$$
        side=SELL,)
# Wrapper for the async event loop to run the blocking code in a separate thread
async def mainhome11():
    buy_response =await place_order_async(order_args1)
    ord= buy_response.get('orderID')
    while True:
      await asyncio.sleep(1)
      order = client.get_order(ord)
      print(order)
      if order.status=="successful":
         order_args1a = MarketOrderArgs(
         price=0.5,
         size=1.0,
         side=BUY,
         token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
         )
         await place_order_async(order_args1a)
         break
async def mainhome1( pri:float):
    count = 1
    order_args1 = MarketOrderArgs(
           token_id="62433812027474946938634419848281832104248932280751877039217144767642305388165",
           amount=1.0 ,   # $$$
           side=BUY,)
    buy_response =await place_order_asyncMarket(order_args1)
    ord= buy_response.get('orderID')
    print(ord)
    while True:
      await asyncio.sleep(1)
      count +=1
      if(count==8):
         resp = client.cancel(order_id=ord)
         print(resp)
         break                                                                                                                                                                                          
      order = client.get_order(ord)
      print(order)
      if order:
         print(order['status'])
         print(order['size_matched'])

         if order['status'] == 'MATCHED':
           await asyncio.sleep(5)
           order_args1a = MarketOrderArgs(
           token_id="62433812027474946938634419848281832104248932280751877039217144767642305388165",
           amount=float(order['size_matched']) ,   # $$$
           side=SELL,)
           await place_order_asyncMarket(order_args1a)
           break
    
         



async def mainaway1( pri:float):
    count = 1
    order_args1 = MarketOrderArgs(
           token_id="30655246989675463473681288974632796744324102944944047413169202262215402786188",
           amount=1.0 ,   # $$$
           side=BUY,)
    buy_response =await place_order_asyncMarket(order_args1)
    ord= buy_response.get('orderID')
    print(ord)
    while True:
      await asyncio.sleep(1)
      count +=1
      if(count==10):
         resp = client.cancel(order_id=ord)
         print(resp)
         break                                                                                                                                                                                          
      order = client.get_order(ord)
      print(order)
      if order:
         print(order['status'])
         print(order['size_matched'])

         if order['status'] == 'MATCHED':
           await asyncio.sleep(5)
           order_args1a = MarketOrderArgs(
           token_id="30655246989675463473681288974632796744324102944944047413169202262215402786188",
           amount=float(order['size_matched']) ,   # $$$
           side=SELL,)
           await place_order_asyncMarket(order_args1a)
           break
async def mainhome2():
    await place_order_async(order_args3)
    await asyncio.sleep(4)
    await place_order_async(order_args3a)
async def mainaway2():
    await place_order_async(order_args4)
    await asyncio.sleep(4)
    await place_order_async(order_args4a)
async def mainhome3():
    await place_order_async(order_args5)
    await asyncio.sleep(4)
    await place_order_async(order_args5a)
async def mainaway3():
    await place_order_async(order_args6)
    await asyncio.sleep(4)
    await place_order_async(order_args6a)
async def mainhome4():
    await place_order_async(order_args7)
    await asyncio.sleep(4)
    await place_order_async(order_args7a)
async def mainaway4():
    await place_order_async(order_args8)
    await asyncio.sleep(4)
    await place_order_async(order_args8a)
async def mainhome5():
    await place_order_async(order_args9)
    await asyncio.sleep(4)
    await place_order_async(order_args9a)
async def mainaway5():
    await place_order_async(order_args10)
    await asyncio.sleep(4)
    await place_order_async(order_args10a)
# Ensures an event loop is running
url = ""
querystring1 = {"event_id": "1605665116"}  #jazz clips
querystring2 = {"event_id": "1604444596"}
querystring3 = {"event_id": "1604444597"}
querystring4 = {"event_id": "1604445363"}
querystring5 = {"event_id": "1604393837"}


# Headers containing your RapidAPI key and the API host
headers = {
    "x-rapidapi-key": "",  # Replace with your actual RapidAPI key
    "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}

# Deque to store the last 10 differences

last_10_differences_dict = {i: deque(maxlen=10) for i in range(5)}
# Function to calculate implied probability from decimal odds
def calculate_implied_probability(decimal_odds):
    return 1 / decimal_odds

# Loop to make the API call every 10 seconds
async def fetch_and_process_data(api_index):

 while True:
    # Make the GET request to the API
    last_10_differences = last_10_differences_dict[api_index]
    checkstring= querystring1
    if api_index ==0:
     checkstring= querystring1
    if api_index ==1:
      checkstring= querystring2
    if api_index ==2:
     checkstring= querystring3
    if api_index ==3:
      checkstring= querystring4
    if api_index ==4:
      checkstring= querystring5
    async with aiohttp.ClientSession() as session:  # Use aiohttp for asynchronous HTTP requests
        
       
        async with session.get(url, headers=headers, params=checkstring) as response:
                if response.status == 200:
                    data = await response.json()
        print({api_index})
    # Check if the response is successful
    

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
                if implied_odds_change > 0 and abs(implied_odds_change) > 7  and abs(implied_odds_change) <= 10:
                    print("The team's chances have improved (higher probability of winning), and the implied probability change is more than 5%, placing orders.")
                    if api_index==0:
                     # place_orders_home1()
                      await mainhome1(last_implied_probability) 
                     
                    if api_index==1:
                     # place_orders_home2()
                      await mainhome2(last_implied_probability)  
                    if api_index==2:
                     # place_orders_home3()
                       await mainhome3(last_implied_probability)  
                    if api_index==3:
                      #place_orders_home4()
                       await mainhome4(last_implied_probability)  
                    if api_index==4:
                       await mainhome5(last_implied_probability)  
                      #place_orders_home5()
                    await send_message()
                    last_10_differences_dict[api_index].clear()
                if implied_odds_change < 0 and abs(implied_odds_change) > 7 and abs(implied_odds_change) <= 10:
                    print("The team's chances have decreased (lower probability of winning), and the implied probability change is more than 5%, placing orders.")
                    if api_index==0:
                     # place_orders_home1()
                      await mainaway1(last_implied_probability)  
                    if api_index==1:
                     # place_orders_home2()
                      await mainaway2(last_implied_probability)  
                    if api_index==2:
                     # place_orders_home3()
                       await mainaway3(last_implied_probability)  
                    if api_index==3:
                      #place_orders_home4()
                       await mainaway4(last_implied_probability)  
                    if api_index==4:
                       await mainaway5(last_implied_probability)  
                      #place_orders_home5()
                    await send_message()
                    last_10_differences_dict[api_index].clear()
                if implied_odds_change > 0 and abs(implied_odds_change) > 10:
                    print("The team's chances have improved (higher probability of winning), and the implied probability change is more than 10%, placing orders.")
                    if api_index==0:
                     # place_orders_home1()
                      await mainhome1(last_implied_probability)  
                    if api_index==1:
                     # place_orders_home2()
                      await mainhome2(last_implied_probability)  
                    if api_index==2:
                     # place_orders_home3()
                       await mainhome3(last_implied_probability)  
                    if api_index==3:
                      #place_orders_home4()
                       await mainhome4(last_implied_probability)  
                    if api_index==4:
                       await mainhome5(last_implied_probability)  
                      #place_orders_home5()
                    await send_message()
                    last_10_differences_dict[api_index].clear()
                if implied_odds_change < 0 and abs(implied_odds_change) > 10:
                    print("The team's chances have decreased (lower probability of winning), and the implied probability change is more than 10%, placing orders.")
                    if api_index==0:
                     # place_orders_home1()
                      await mainaway1(last_implied_probability)  
                    if api_index==1:
                     # place_orders_home2()
                      await mainaway2(last_implied_probability)  
                    if api_index==2:
                     # place_orders_home3()
                       await mainaway3(last_implied_probability)  
                    if api_index==3:
                      #place_orders_home4()
                       await mainaway4(last_implied_probability)  
                    if api_index==4:
                       await mainaway5(last_implied_probability)  
                      #place_orders_home5()
                    await send_message()
                    last_10_differences_dict[api_index].clear()
          else:
                    print("iuhidg")
                    last_10_differences_dict[api_index].clear()
         else:
                print("Moneyline is not available for this event.")
                last_10_differences_dict[api_index].clear()
        else:
            print("No events data available.")
            last_10_differences_dict[api_index].clear()
 else:
        print(f"Failed to fetch data: {response.status_code}")
    
async def start_multiple_tasks():
    tasks = []
    for i in range(1):  # 5 different API calls
        tasks.append(asyncio.create_task(fetch_and_process_data(i)))
    await asyncio.gather(*tasks)

# Run the tasks
asyncio.run(start_multiple_tasks())
