import sqlite3


# Create a connection to the SQLite database
def create_connection():
    return sqlite3.connect("university.db")


# Create all required tables
def create_tables():

    conn = create_connection()
    cursor = conn.cursor()

    # Student table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT,
            email TEXT
        )
    """)

    # Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL
        )
    """)

    # Lecturer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT
        )
    """)

    # Subject table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY,
            subject_code TEXT NOT NULL,
            subject_name TEXT NOT NULL
        )
    """)

    # Lecture table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lectures (
            lecture_id INTEGER PRIMARY KEY,
            lecture_name TEXT NOT NULL,
            subject_id INTEGER,
            lecturer_id INTEGER,

            FOREIGN KEY (subject_id)
                REFERENCES subjects(subject_id),

            FOREIGN KEY (lecturer_id)
                REFERENCES lecturers(lecturer_id)
        )
    """)

    # Enrollment connects students and courses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date TEXT,

            FOREIGN KEY (student_id)
                REFERENCES students(student_id),

            FOREIGN KEY (course_id)
                REFERENCES courses(course_id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database tables created successfully.")