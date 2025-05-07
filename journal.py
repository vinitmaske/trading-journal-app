import sqlite3

# ✅ Step 1: Connect to a local SQLite database
# If it doesn't exist, this will create it
conn = sqlite3.connect("trading_journal.db")

# ✅ Step 2: Create a table for trades (if it doesn't already exist)
conn.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock TEXT NOT NULL,
        entry_price REAL NOT NULL,
        stoploss REAL NOT NULL,
        target REAL NOT NULL,
        quantity INTEGER NOT NULL,
        entry_date TEXT NOT NULL,
        status TEXT NOT NULL
    );
""")

# ✅ Step 3: Add a sample trade
sample_trade = {
    "stock": "TCS",
    "entry_price": 3600,
    "stoploss": 3500,
    "target": 3800,
    "quantity": 10,
    "entry_date": "2025-05-06",
    "status": "open"
}

# ✅ Step 4: Insert the sample trade into the table
conn.execute("""
    INSERT INTO trades (stock, entry_price, stoploss, target, quantity, entry_date, status)
    VALUES (?, ?, ?, ?, ?, ?, ?);
""", (
    sample_trade["stock"],
    sample_trade["entry_price"],
    sample_trade["stoploss"],
    sample_trade["target"],
    sample_trade["quantity"],
    sample_trade["entry_date"],
    sample_trade["status"]
))

# ✅ Step 5: Save changes and close the database
conn.commit()
conn.close()

print("🎉 Sample trade saved to the database successfully!")
