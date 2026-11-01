import os
import requests
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_btc_price():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        return r['bitcoin']['usd']
    except:
        return 0

def send_msg(text):
    requests.get(f"{API_URL}/sendMessage", params={"chat_id": "@btc_signal_shahid2100", "text": text})

# Bot start
price = get_btc_price()
if price > 0:
    send_msg(f"🚀 BTC Signal Bot LIVE!\nBTC Price: ${price}\n\nBot by Shahid is running 24/7 ✅")

# Keep bot running for 5 hours
start = time.time()
while time.time() - start < 17000: # 4.7 hours
    time.sleep(60)
