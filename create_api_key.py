from py_clob_client.client import ClobClient
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY
import os
# Define the host, private key, and chain ID
host = "https://clob.polymarket.com"
private_key = ""
chain_id = 137  # Polygon Mainnet
variable_value = os.getenv('PRIVATE_KEY')
# Initialize the client with private key
client = ClobClient(host, key=private_key, chain_id=chain_id)

# Create the API key
api_key_data = client.create_or_derive_api_creds()

# Print the API key data
print("API Key Data:", api_key_data)
