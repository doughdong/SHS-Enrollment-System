import enrollment


def main():
    while True:
        print("\n==============================")
        print("     SHS ENROLLMENT SYSTEM")
        print("==============================")
        print("1. Enroll Student")
        print("2. View Enrolled Students")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            enrollment.add_student()

        elif choice == "2":
            enrollment.view_students()

        elif choice == "3":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please choose 1-3.")


main()