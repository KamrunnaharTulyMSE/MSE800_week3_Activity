# OOP Inheritance Project Using Python

## Purpose
This project demonstrates Object-Oriented Programming (OOP) inheritance using a simple university staff hierarchy.

## Class Hierarchy

Person
|
└── Staff
    ├── General
    └── Academic
        └── Lecturer

## Main Classes

- **Person**: Stores common `id` and `name`.
- **Staff**: Inherits from Person and stores `staff_id` and `tax_num`.
- **General**: Inherits from Staff and calculates/displays the pay rate.
- **Academic**: Inherits from Staff and stores/calculates publications.
- **Lecturer**: Inherits from Academic and displays the number of publications.

## OOP Concepts Used

- Classes
- Objects
- Attributes
- Methods
- Inheritance
- `super()` for calling parent constructors

## How to Run

Open a terminal in this folder and run:

```bash
python main.py
```

## Program Output

```text
=== University Staff Information ===
Lecturer: Dr. Sarah Lee
Number of Publications: 12

General Staff: John Smith
Pay Rate: $28.50 per hour
```
