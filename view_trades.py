import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect("trading_journal.db")
cursor = conn.cursor()

# Step 2: Read all trades from the table
cursor.execute("SELECT * FROM trades")
trades = cursor.fetchall()

# Step 3: Display trades
if trades:
    print("\n📋 Saved Trades:\n")
    for trade in trades:
        print(f"🆔 ID: {trade[0]}")
        print(f"📈 Stock: {trade[1]}")
        print(f"💰 Entry Price: {trade[2]}")
        print(f"🛑 Stoploss: {trade[3]}")
        print(f"🎯 Target: {trade[4]}")
        print(f"📦 Quantity: {trade[5]}")
        print(f"🗓️ Entry Date: {trade[6]}")
        print(f"🔖 Status: {trade[7]}")
        print("-" * 40)
else:
    print("⚠️ No trades found in the database.")

# Step 4: Close the connection
conn.close()
