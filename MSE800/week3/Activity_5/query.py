import sqlite3


def run_queries():

    connection = sqlite3.connect("money_exchange.db")
    cursor = connection.cursor()

    # Query 1: Show all customers
    print("\n--- Customers ---")

    cursor.execute("""
        SELECT customer_id, name, phone, email
        FROM Customer
    """)

    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    # Query 2: Show all currencies
    print("\n--- Currencies ---")

    cursor.execute("""
        SELECT currency_id, currency_code, currency_name
        FROM Currency
    """)

    currencies = cursor.fetchall()

    for currency in currencies:
        print(currency)

    # Query 3: Show exchange rates
    print("\n--- Exchange Rates ---")

    cursor.execute("""
        SELECT
            c1.currency_code,
            c2.currency_code,
            e.rate,
            e.rate_date
        FROM ExchangeRate e
        JOIN Currency c1
            ON e.from_currency_id = c1.currency_id
        JOIN Currency c2
            ON e.to_currency_id = c2.currency_id
    """)

    rates = cursor.fetchall()

    for rate in rates:
        print(rate)

    # Query 4: Show all exchange transactions
    print("\n--- Exchange Transactions ---")

    cursor.execute("""
        SELECT
            t.transaction_id,
            c.name,
            c1.currency_code,
            c2.currency_code,
            t.amount,
            t.exchange_rate,
            t.converted_amount,
            t.transaction_date
        FROM ExchangeTransaction t
        JOIN Customer c
            ON t.customer_id = c.customer_id
        JOIN Currency c1
            ON t.from_currency_id = c1.currency_id
        JOIN Currency c2
            ON t.to_currency_id = c2.currency_id
    """)

    transactions = cursor.fetchall()

    for transaction in transactions:
        print(transaction)

    connection.close()


if __name__ == "__main__":
    run_queries()