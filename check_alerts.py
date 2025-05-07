import sqlite3
from nsetools import Nse
import time

# Initialize NSE tools
nse = Nse()

# Connect to your database
conn = sqlite3.connect("trading_journal.db")
cursor = conn.cursor()

# Get all open trades
cursor.execute("SELECT * FROM trades WHERE status = 'open'")
open_trades = cursor.fetchall()

print("\n🔍 Checking open trades...\n")

for trade in open_trades:
    trade_id = trade[0]
    stock = trade[1]
    entry_price = trade[2]
    stoploss = trade[3]
    target = trade[4]
    quantity = trade[5]

    try:
        # NSE symbols are usually in uppercase
        stock_data = nse.get_quote(stock.upper())
        current_price = stock_data['lastPrice']

        print(f"📈 {stock} Current Price: ₹{current_price}")

        # Check Stoploss hit
        if current_price <= stoploss:
            print(f"❌ STOPLOSS HIT for {stock}! (₹{current_price} ≤ ₹{stoploss})")

        # Check Target hit
        elif current_price >= target:
            print(f"🎯 TARGET HIT for {stock}! (₹{current_price} ≥ ₹{target})")

        else:
            print(f"🕒 No action needed for {stock}.")

        print("-" * 40)

    except Exception as e:
        print(f"⚠️ Error fetching price for {stock}: {e}")
        print("-" * 40)

conn.close()
