import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("money_exchange.db")
        self.cursor = self.connection.cursor()

    def create_tables(self):

        # Customer table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customer (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        """)

        # Currency table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Currency (
                currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                currency_code TEXT NOT NULL UNIQUE,
                currency_name TEXT NOT NULL
            )
        """)

        # Exchange Rate table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ExchangeRate (
                rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_currency_id INTEGER NOT NULL,
                to_currency_id INTEGER NOT NULL,
                rate REAL NOT NULL,
                rate_date TEXT NOT NULL,

                FOREIGN KEY (from_currency_id)
                    REFERENCES Currency(currency_id),

                FOREIGN KEY (to_currency_id)
                    REFERENCES Currency(currency_id)
            )
        """)

        # Exchange Transaction table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ExchangeTransaction (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                from_currency_id INTEGER NOT NULL,
                to_currency_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                exchange_rate REAL NOT NULL,
                converted_amount REAL NOT NULL,
                transaction_date TEXT NOT NULL,

                FOREIGN KEY (customer_id)
                    REFERENCES Customer(customer_id),

                FOREIGN KEY (from_currency_id)
                    REFERENCES Currency(currency_id),

                FOREIGN KEY (to_currency_id)
                    REFERENCES Currency(currency_id)
            )
        """)

        self.connection.commit()
        print("Database tables created successfully.")

    def close(self):
        self.connection.close()