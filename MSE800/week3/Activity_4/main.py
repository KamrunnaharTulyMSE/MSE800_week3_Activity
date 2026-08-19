import sqlite3


# Connect to the SQLite database.
# If university.db does not exist, SQLite will create it.
connection = sqlite3.connect("university.db")

cursor = connection.cursor()


# -------------------------------------------------
# Create the database tables
# -------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS lecturers (
    lecturer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id)
)
""")


print("Database tables created successfully.")


# -------------------------------------------------
# Insert sample courses
# INSERT OR IGNORE prevents duplicate records
# when the program is run again.
# -------------------------------------------------

courses = [
    (1, "Software Engineering"),
    (2, "Database Systems"),
    (3, "Artificial Intelligence")
]

cursor.executemany("""
INSERT OR IGNORE INTO courses (course_id, course_name)
VALUES (?, ?)
""", courses)


# -------------------------------------------------
# Insert 5 students
# -------------------------------------------------

students = [
    (1, "Alice", "Johnson"),
    (2, "Ben", "Carter"),
    (3, "Chloe", "Wilson"),
    (4, "Daniel", "Kim"),
    (5, "Emma", "Brown")
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(student_id, first_name, last_name)
VALUES (?, ?, ?)
""", students)


# -------------------------------------------------
# Insert 2 lecturers
# -------------------------------------------------

lecturers = [
    (1, "John", "Smith"),
    (2, "Sarah", "Williams")
]

cursor.executemany("""
INSERT OR IGNORE INTO lecturers
(lecturer_id, first_name, last_name)
VALUES (?, ?, ?)
""", lecturers)


# -------------------------------------------------
# Insert enrolment records
#
# Some students are enrolled in more than one
# course so that Question 2 can be answered.
# -------------------------------------------------

enrollments = [
    (1, 1),  # Alice -> Software Engineering
    (1, 2),  # Alice -> Database Systems

    (2, 1),  # Ben -> Software Engineering
    (2, 3),  # Ben -> Artificial Intelligence

    (3, 2),  # Chloe -> Database Systems

    (4, 3),  # Daniel -> Artificial Intelligence

    (5, 1),  # Emma -> Software Engineering
    (5, 2),  # Emma -> Database Systems
    (5, 3)   # Emma -> Artificial Intelligence
]

cursor.executemany("""
INSERT OR IGNORE INTO enrollments
(student_id, course_id)
VALUES (?, ?)
""", enrollments)


# Save all changes.
connection.commit()

print("Sample data inserted successfully.")


# Close the database connection.
connection.close()

print("Database connection closed.")