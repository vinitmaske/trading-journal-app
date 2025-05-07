import sqlite3

# --- Setup: Create the database and table if it doesn't exist ---
def setup_database():
    conn = sqlite3.connect("trading_journal.db")
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
    conn.commit()
    conn.close()

# --- Option 1: Add a new trade ---
def add_trade():
    print("\n📥 Enter Trade Details:")
    stock = input("Stock name (e.g., TCS): ")
    entry_price = float(input("Entry price: "))
    stoploss = float(input("Stoploss: "))
    target = float(input("Target: "))
    quantity = int(input("Quantity: "))
    entry_date = input("Entry date (YYYY-MM-DD): ")
    status = "open"  # All new trades are open by default

    conn = sqlite3.connect("trading_journal.db")
    conn.execute("""
        INSERT INTO trades (stock, entry_price, stoploss, target, quantity, entry_date, status)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (stock, entry_price, stoploss, target, quantity, entry_date, status))
    conn.commit()
    conn.close()

    print("✅ Trade added successfully!\n")

# --- Option 2: View all trades ---
def view_trades():
    conn = sqlite3.connect("trading_journal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trades")
    trades = cursor.fetchall()
    conn.close()

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
        print("⚠️ No trades found.\n")

# --- Main Menu Loop ---
def run_app():
    setup_database()
    while True:
        print("\n🔷 TRADING JOURNAL MENU 🔷")
        print("1. Add a New Trade")
        print("2. View All Trades")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            add_trade()
        elif choice == "2":
            view_trades()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# --- Start the app ---
if __name__ == "__main__":
    run_app()

