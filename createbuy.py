from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY
from py_clob_client.order_builder.constants import SELL
host = "https://clob.polymarket.com"
private_key = ""
chain_id = 137  # Polygon Mainnet
client = ClobClient(host, key=private_key, chain_id=chain_id)


BuyCelts = client.create_and_post_order(
    OrderArgs(
       
        size=10.0,
        side=BUY,
        token_id="60946109457844311082143907314289048218416649112897669299714218710543184985807", # buy celts
    )
)
BuyCavs = client.create_and_post_order(
    OrderArgs(
       
        size=10.0,
        side=BUY,
        token_id="52706774248302195740980640980239240497601699396779667176559712933101126831788", # buy cavs
    )
)
SellCelts = client.create_and_post_order(
    OrderArgs(
       
        size=10.0,
        side=SELL,
        token_id="60946109457844311082143907314289048218416649112897669299714218710543184985807", # sell celts
    )
)
SellCavs = client.create_and_post_order(
    OrderArgs(
       
        size=10.0,
        side=SELL,
        token_id="52706774248302195740980640980239240497601699396779667176559712933101126831788", # sell cavs
    )
)
print(BuyCelts)