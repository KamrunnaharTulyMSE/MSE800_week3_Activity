import sqlite3


# Question 1:
# Count how many students are registered in each course.
COURSE_REGISTRATION_COUNTS_SQL = """
SELECT
    c.course_id,
    c.course_name,
    COUNT(e.student_id) AS student_count
FROM courses AS c
LEFT JOIN enrollments AS e
    ON e.course_id = c.course_id
GROUP BY
    c.course_id,
    c.course_name
ORDER BY
    c.course_id;
"""


# Question 2:
# Find students who have enrolled in more than one course.
MULTI_COURSE_STUDENTS_SQL = """
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS course_count
FROM students AS s
JOIN enrollments AS e
    ON e.student_id = s.student_id
GROUP BY
    s.student_id,
    s.first_name,
    s.last_name
HAVING COUNT(e.course_id) > 1
ORDER BY
    s.student_id;
"""


# Connect to the SQLite database.
connection = sqlite3.connect("university.db")

# Create a cursor to execute SQL queries.
cursor = connection.cursor()


# Run Question 1 query.
print("\n--- Students Registered in Each Course ---")

cursor.execute(COURSE_REGISTRATION_COUNTS_SQL)

for row in cursor.fetchall():
    print(row)


# Run Question 2 query.
print("\n--- Students Enrolled in More Than One Course ---")

cursor.execute(MULTI_COURSE_STUDENTS_SQL)

for row in cursor.fetchall():
    print(row)


# Close the database connection.
connection.close()