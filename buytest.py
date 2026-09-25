from py_clob_client.client import ClobClient
from py_clob_client.client import ApiCreds
from py_clob_client.clob_types import OrderArgs
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY
from py_clob_client.order_builder.constants import SELL
from py_clob_client.clob_types import MarketOrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY
import os
host = "https://clob.polymarket.com"
private_key = "0xd29e629f6d71aacad6ee5b15f026de711451575db881d456b068c55e2b728a94"
chain_id = 137  # Polygon Mainnet
variable_value = os.getenv('PRIVATE_KEY')
creds1 = ApiCreds(
                api_key="122380e4-1720-ec43-ec56-5052b6fd7c41",
                api_secret="HRUfMWUnd20zs4A22hQDkrzPbWioHoZkHJlueCkKQaY=",
                api_passphrase="29fa091d5f74b9875b573e410e9554eb76624cc350b0bbe5340d625fff07e0a3",
)

client = ClobClient(host, key=private_key, chain_id=chain_id, creds= creds1,signature_type=1, funder="0xf7777B2D3f6E9603486B6CEEBC2187E4666a34a5" )

#BuyCelts = client.create_and_post_order(
    #OrderArgs(
       
     #   size=1.0,
      #  side=BUY,
      #  token_id="11507159231830295039122966477045231182687709262227577586796015773438035183698", # buy celts
  #  )
#)
order_args1 = MarketOrderArgs(
    token_id="11507159231830295039122966477045231182687709262227577586796015773438035183698",
    amount=1.0,  # $$$
    side=BUY,
   
)
order_args2 = MarketOrderArgs(
    token_id="11507159231830295039122966477045231182687709262227577586796015773438035183698",
    amount=1.0,  # $$$
    side=SELL,
   
)
order_args3 = MarketOrderArgs(
    token_id="11507159231830295039122966477045231182687709262227577586796015773438035183698",
    amount=1.0,  # $$$
    side=BUY,
   
)
order_args4 = MarketOrderArgs(
    token_id="11507159231830295039122966477045231182687709262227577586796015773438035183698",
    amount=1.0,  # $$$
    side=SELL,
   
)
# Assuming 'client' is already initialized and authorized to send orders
signed_order = client.create_market_order(order_args1)
print(signed_order)
resp = client.post_order(signed_order, OrderType.FOK)
print(resp)