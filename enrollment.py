import database

ACADEMIC_STRANDS = [
    "STEM",
    "ABM",
    "HUMSS",
    "GAS"
]

TVL_STRANDS = [
    "ICT - Programming",
    "ICT - CSS"
]

GENDERS = [
    "Male",
    "Female"
]

GRADE_LEVELS = [
    "Grade 11",
    "Grade 12"
]

TRACKS = [
    "Academic",
    "TVL"
]

def validate_student(student):

    required_fields = [
        "student_id",
        "first_name",
        "last_name",
        "age",
        "gender",
        "grade_level",
        "track",
        "strand",
        "contact",
        "address",
        "guardian"
    ]

    for field in required_fields:

        if str(student.get(field, "")).strip() == "":
            field_name = field.replace("_", " ").title()

            return False, field_name + " cannot be empty."

    if student["gender"] not in GENDERS:
        return False, "Invalid gender. Please choose Male or Female."

    # Validate grade level
    if student["grade_level"] not in GRADE_LEVELS:
        return False, "Invalid grade level."

    if student["track"] not in TRACKS:
        return False, "Invalid track."

    if student["track"] == "Academic":

        if student["strand"] not in ACADEMIC_STRANDS:
            return False, "Invalid Academic strand."

    elif student["track"] == "TVL":

        if student["strand"] not in TVL_STRANDS:
            return False, "Invalid TVL strand."

    try:
        age_number = int(student["age"])

        if age_number <= 0:
            return False, "Age must be greater than 0."

    except ValueError:
        return False, "Invalid age. Please enter a number."

    if not str(student["contact"]).isdigit():
        return False, "Invalid contact number. Please enter numbers only."

    return True, "Valid student."


def enroll_student(student):

    valid, message = validate_student(student)

    if not valid:
        return False, message

    # Save the student into SQLite
    return database.add_student(student)

def get_all_students():

    return database.get_students()