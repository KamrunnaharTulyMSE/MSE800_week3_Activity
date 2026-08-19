# Money Exchange System

## Project Description

This project is a simple **Money Exchange System** developed using Python, SQLite3, and Object-Oriented Programming (OOP).

The system is designed to help a money exchange business manage customers, currencies, exchange rates, and currency exchange transactions.

## Database Tables

I created **4 tables** for this project:

1. Customer

The `Customer` table stores information about customers who use the money exchange service. 

This table is necessary because the system needs to store customer information and identify which customer made each currency exchange transaction.

Attributes:
- `customer_id` - Primary Key
- `name` - Customer's name
- `phone` - Customer's phone number
- `email` - Customer's email


2. Currency

The `Currency` table stores information about the currencies supported by the money exchange business.

This table is necessary because the money exchange system needs to manage different currencies. It also allows other tables to refer to currencies using foreign keys.

Attributes:
- `currency_id` - Primary Key
- `currency_code` - Currency code, such as USD, NZD, or BDT
- `currency_name` - Full name of the currency


3. ExchangeRate

The `ExchangeRate` table stores exchange rates between different currencies.

This table is necessary because exchange rates can differ between currency pairs and can change over time. A separate table allows the system to store and manage different rates.

**Attributes:**
- `rate_id` - Primary Key
- `from_currency_id` - Foreign Key
- `to_currency_id` - Foreign Key
- `rate` - Exchange rate
- `rate_date` - Date of the exchange rate


4. Transaction

The `Transaction` table stores the actual currency exchange transactions made by customers.

This table is necessary because the system needs to keep a record of every currency exchange made by a customer. 
It connects the customer, currencies, amount, exchange rate, and transaction date together.

**Attributes:**
- `transaction_id` - Primary Key
- `customer_id` - Foreign Key
- `from_currency_id` - Foreign Key
- `to_currency_id` - Foreign Key
- `amount` - Amount being exchanged
- `exchange_rate` - Rate used for the transaction
- `converted_amount` - Final converted amount
- `transaction_date` - Date of the transaction

Relationships:

Customer and Transaction: One-to-Many (1:N)

One customer can make many transactions, but each transaction belongs to one customer.

Currency and Transaction: One-to-Many (1:N)

One currency can be used in many transactions. A transaction has both a source currency and a destination currency.

Currency and ExchangeRate: One-to-Many (1:N)

One currency can be involved in many exchange-rate records. A currency can appear as either the source or destination currency.

## Primary Keys and Foreign Keys

Primary Key (PK):Uniquely identifies each record in a table.
Foreign Key (FK):Refers to a primary key in another table and creates a relationship between tables.

## Technologies Used

- Python
- SQLite3
- SQL
- Object-Oriented Programming (OOP)