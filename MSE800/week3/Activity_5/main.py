from database import Database


def insert_sample_data(db):

    # Add customers
    customers = [
        ("Alice Johnson", "0211111111", "alice@email.com"),
        ("Bob Smith", "0222222222", "bob@email.com"),
        ("Charlie Brown", "0233333333", "charlie@email.com")
    ]

    db.cursor.executemany("""
        INSERT OR IGNORE INTO Customer (name, phone, email)
        VALUES (?, ?, ?)
    """, customers)

    # Add currencies
    currencies = [
        ("NZD", "New Zealand Dollar"),
        ("USD", "US Dollar"),
        ("AUD", "Australian Dollar"),
        ("EUR", "Euro")
    ]

    db.cursor.executemany("""
        INSERT OR IGNORE INTO Currency (currency_code, currency_name)
        VALUES (?, ?)
    """, currencies)

    # Add exchange rates
    rates = [
        (1, 2, 0.60, "2026-08-20"),
        (1, 3, 0.92, "2026-08-20"),
        (1, 4, 0.52, "2026-08-20"),
        (2, 1, 1.67, "2026-08-20"),
        (3, 1, 1.09, "2026-08-20"),
        (4, 1, 1.92, "2026-08-20")
    ]

    db.cursor.executemany("""
        INSERT OR IGNORE INTO ExchangeRate
        (from_currency_id, to_currency_id, rate, rate_date)
        VALUES (?, ?, ?, ?)
    """, rates)

    # Add exchange transactions
    transactions = [
        (1, 1, 2, 1000, 0.60, 600, "2026-08-20"),
        (2, 1, 3, 500, 0.92, 460, "2026-08-20"),
        (3, 2, 1, 300, 1.67, 501, "2026-08-20"),
        (1, 1, 4, 200, 0.52, 104, "2026-08-20")
    ]

    db.cursor.executemany("""
        INSERT INTO ExchangeTransaction
        (customer_id, from_currency_id, to_currency_id,
         amount, exchange_rate, converted_amount, transaction_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, transactions)

    db.connection.commit()

    print("Sample data inserted successfully.")


def main():

    db = Database()

    db.create_tables()

    insert_sample_data(db)

    db.close()

    print("Database connection closed.")


if __name__ == "__main__":
    main()