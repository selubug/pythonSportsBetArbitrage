import asyncio
from telegram import Bot

# Setup for the Polymarket API (ClobClient)
host = "https://clob.polymarket.com"
private_key = "0xd29e629f6d71aacad6ee5b15f026de711451575db881d456b068c55e2b728a94"
chain_id = 137  # Polygon Mainnet

bot_token = '7587403778:AAGDMdG_Yf8jn-pkZ3xtoZZ46hsyLsIf0CI'
chat_id = '7107063732'

async def send_message():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text="BUY ORDER")

# Run the event loop
asyncio.run(send_message())