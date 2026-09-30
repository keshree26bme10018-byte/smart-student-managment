
import csv
import os

FILE_NAME = "students.csv"


def add_student():
    print("\n--- Add New Student ---")

    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    marks = input("Enter Marks (out of 100): ").strip()

    # Check that no field is empty
    if not roll_no or not name or not branch or not marks:
        print("Error: All fields are required!")
        return

    # Validate marks
    try:
        marks = float(marks)
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Please enter marks as a number.")
        return

    # Check for duplicate roll numbers
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for student in reader:
                if student["Roll Number"] == roll_no:
                    print("Error: Roll number already exists!")
                    return

    # Save the student to the CSV file
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        fields = ["Roll Number", "Name", "Branch", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Roll Number": roll_no,
            "Name": name,
            "Branch": branch,
            "Marks": marks
        })

    print("\nStudent added successfully!")


# Main program
print("Welcome to Smart Student Management System!")

while True:
    print("\n1. Add Student")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")