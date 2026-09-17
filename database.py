import sqlite3

DATABASE_NAME = "shs_enrollment.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            grade_level TEXT NOT NULL,
            track TEXT NOT NULL,
            strand TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT NOT NULL,
            guardian TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Enrolled',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            setting_name TEXT PRIMARY KEY,
            setting_value TEXT NOT NULL
        )
    """)

    defaults = [
        ("school_name", "SHS Enrollment System"),
        ("school_year", "2026-2027"),
        ("enrollment_status", "OPEN")
    ]

    for name, value in defaults:
        cursor.execute(
            "INSERT OR IGNORE INTO settings (setting_name, setting_value) VALUES (?, ?)",
            (name, value)
        )

    connection.commit()
    connection.close()


def add_student(student):
    connection = get_connection()
    try:
        connection.execute("""
            INSERT INTO students (
                student_id, first_name, middle_name, last_name, age,
                gender, grade_level, track, strand, contact, address, guardian
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student["student_id"], student["first_name"], student["middle_name"],
            student["last_name"], student["age"], student["gender"],
            student["grade_level"], student["track"], student["strand"],
            student["contact"], student["address"], student["guardian"]
        ))
        connection.commit()
        return True, "Student enrolled successfully."
    except sqlite3.IntegrityError:
        return False, "Student ID already exists."
    finally:
        connection.close()


def get_students(search_text=""):
    connection = get_connection()
    if search_text.strip():
        value = "%" + search_text.strip() + "%"
        cursor = connection.execute("""
            SELECT * FROM students
            WHERE student_id LIKE ? OR first_name LIKE ? OR last_name LIKE ?
            ORDER BY id DESC
        """, (value, value, value))
    else:
        cursor = connection.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()
    connection.close()
    return students


def get_student(student_id):
    connection = get_connection()
    student = connection.execute(
        "SELECT * FROM students WHERE student_id = ?", (student_id,)
    ).fetchone()
    connection.close()
    return student


def update_student(student_id, student):
    connection = get_connection()
    connection.execute("""
        UPDATE students SET first_name = ?, middle_name = ?, last_name = ?,
        age = ?, gender = ?, grade_level = ?, track = ?, strand = ?,
        contact = ?, address = ?, guardian = ? WHERE student_id = ?
    """, (
        student["first_name"], student["middle_name"], student["last_name"],
        student["age"], student["gender"], student["grade_level"],
        student["track"], student["strand"], student["contact"],
        student["address"], student["guardian"], student_id
    ))
    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = get_connection()
    connection.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    connection.commit()
    connection.close()


def get_student_count():
    connection = get_connection()
    count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    connection.close()
    return count


def get_setting(name):
    connection = get_connection()
    row = connection.execute(
        "SELECT setting_value FROM settings WHERE setting_name = ?", (name,)
    ).fetchone()
    connection.close()
    return row["setting_value"] if row else ""


def update_setting(name, value):
    connection = get_connection()
    connection.execute("""
        INSERT INTO settings (setting_name, setting_value) VALUES (?, ?)
        ON CONFLICT(setting_name) DO UPDATE SET setting_value = excluded.setting_value
    """, (name, value))
    connection.commit()
    connection.close()
