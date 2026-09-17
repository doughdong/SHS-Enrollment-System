import sqlite3


DATABASE_NAME = "students.db"


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

            age TEXT NOT NULL,

            gender TEXT NOT NULL,

            grade_level TEXT NOT NULL,

            track TEXT NOT NULL,

            strand TEXT NOT NULL,

            contact TEXT NOT NULL,

            address TEXT NOT NULL,

            guardian TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def add_student(student):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (

                student_id,
                first_name,
                middle_name,
                last_name,
                age,
                gender,
                grade_level,
                track,
                strand,
                contact,
                address,
                guardian

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            student["student_id"],
            student["first_name"],
            student["middle_name"],
            student["last_name"],
            student["age"],
            student["gender"],
            student["grade_level"],
            student["track"],
            student["strand"],
            student["contact"],
            student["address"],
            student["guardian"]

        ))

        connection.commit()

        connection.close()

        return True, "Student enrolled successfully."

    except sqlite3.IntegrityError:

        return False, "Student ID already exists."

    except sqlite3.Error as error:

        return False, "Database error: " + str(error)


def get_students():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT

            student_id,
            first_name,
            middle_name,
            last_name,
            age,
            gender,
            grade_level,
            track,
            strand,
            contact,
            address,
            guardian

        FROM students

        ORDER BY id DESC
    """)

    students = []

    for row in cursor.fetchall():

        students.append(dict(row))

    connection.close()

    return students


def get_student(student_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = ?
        """,
        (student_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row:

        return dict(row)

    return None

def update_student(student_id, student):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE students

            SET

                first_name = ?,
                middle_name = ?,
                last_name = ?,
                age = ?,
                gender = ?,
                grade_level = ?,
                track = ?,
                strand = ?,
                contact = ?,
                address = ?,
                guardian = ?

            WHERE student_id = ?
        """, (

            student["first_name"],
            student["middle_name"],
            student["last_name"],
            student["age"],
            student["gender"],
            student["grade_level"],
            student["track"],
            student["strand"],
            student["contact"],
            student["address"],
            student["guardian"],
            student_id

        ))

        connection.commit()

        changed = cursor.rowcount > 0

        connection.close()

        if changed:

            return True, "Student updated successfully."

        return False, "Student not found."

    except sqlite3.Error as error:

        return False, "Database error: " + str(error)


def delete_student(student_id):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = ?
            """,
            (student_id,)
        )

        connection.commit()

        changed = cursor.rowcount > 0

        connection.close()

        if changed:

            return True, "Student deleted successfully."

        return False, "Student not found."

    except sqlite3.Error as error:

        return False, "Database error: " + str(error)

def get_student_count():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count