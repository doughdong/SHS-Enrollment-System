students = []


def add_student():
    print("\n===== STUDENT ENROLLMENT =====")

    while True:
        student_id = input("Student ID: ")

        if student_id != "":
            break

        print("Student ID cannot be empty.")

    while True:
        first_name = input("First Name: ")

        if first_name != "":
            break

        print("First Name cannot be empty.")

    middle_name = input("Middle Name: ")

    while True:
        last_name = input("Last Name: ")

        if last_name != "":
            break

        print("Last Name cannot be empty.")

    while True:
        age = input("Age: ")

        if age.isdigit():
            break

        print("Invalid age. Please enter a number.")

    while True:
        gender = input("Gender (Male/Female): ").lower()

        if gender == "male" or gender == "female":
            gender = gender.capitalize()
            break

        print("Invalid gender. Please enter Male or Female.")

    while True:
        grade_level = input("Grade Level (11/12): ")

        if grade_level == "11" or grade_level == "12":
            grade_level = "Grade " + grade_level
            break

        print("Invalid grade level. Please enter 11 or 12.")

    track, strand = choose_strand()

    while True:
        contact = input("Contact Number: ")

        if contact.isdigit():
            break

        print("Invalid contact number. Please enter numbers only.")

    while True:
        address = input("Address: ")

        if address != "":
            break

        print("Address cannot be empty.")

    while True:
        guardian = input("Guardian: ")

        if guardian != "":
            break

        print("Guardian cannot be empty.")

    student = {
        "student_id": student_id,
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "grade_level": grade_level,
        "track": track,
        "strand": strand,
        "contact": contact,
        "address": address,
        "guardian": guardian
    }

    if validate_student(student):
        students.append(student)
        print("\nStudent enrolled successfully!")


def choose_strand():
    while True:
        print("\n===== TRACK =====")
        print("1. Academic")
        print("2. TVL")

        track_choice = input("Choose track: ")

        if track_choice == "1":
            track = "Academic"

            print("\n===== ACADEMIC STRANDS =====")
            print("1. STEM")
            print("2. ABM")
            print("3. HUMSS")
            print("4. GAS")

            strand_choice = input("Choose strand: ")

            if strand_choice == "1":
                return track, "STEM"
            elif strand_choice == "2":
                return track, "ABM"
            elif strand_choice == "3":
                return track, "HUMSS"
            elif strand_choice == "4":
                return track, "GAS"
            else:
                print("Invalid strand. Please choose 1-4.")

        elif track_choice == "2":
            track = "TVL"

            print("\n===== TVL STRANDS =====")
            print("1. ICT - Programming")
            print("2. ICT - CSS")

            strand_choice = input("Choose strand: ")

            if strand_choice == "1":
                return track, "ICT - Programming"
            elif strand_choice == "2":
                return track, "ICT - CSS"
            else:
                print("Invalid strand. Please choose 1-2.")

        else:
            print("Invalid track. Please choose 1 or 2.")


def validate_student(student):
    if student["student_id"] == "":
        return False

    if student["first_name"] == "":
        return False

    if student["last_name"] == "":
        return False

    if student["age"] == "":
        return False

    if student["gender"] == "":
        return False

    if student["grade_level"] == "":
        return False

    if student["track"] == "":
        return False

    if student["strand"] == "":
        return False

    if student["contact"] == "":
        return False

    if student["address"] == "":
        return False

    if student["guardian"] == "":
        return False

    return True


def view_students():
    print("\n===== ENROLLED STUDENTS =====")

    if len(students) == 0:
        print("No students enrolled.")
        return

    for student in students:
        print("\n------------------------------")
        print("Student ID:", student["student_id"])
        print("Name:", student["first_name"], student["middle_name"], student["last_name"])
        print("Age:", student["age"])
        print("Gender:", student["gender"])
        print("Grade Level:", student["grade_level"])
        print("Track:", student["track"])
        print("Strand:", student["strand"])
        print("Contact:", student["contact"])
        print("Address:", student["address"])
        print("Guardian:", student["guardian"])
        print("------------------------------")