print("=====================================")
print("Welcome to School Attendance System!")
print("=====================================")


class Student:

    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.total_classes = 0
        self.attended_classes = 0

    def mark_attendance(self, status):
        self.total_classes += 1

        if status == "present":
            self.attended_classes += 1

    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0

        return (self.attended_classes / self.total_classes) * 100

    def display(self):
        print(
            f"{self.roll_number:<10}"
            f"{self.name:<15}"
            f"{self.attended_classes:<15}"
            f"{self.total_classes:<10}"
        )


class AttendanceSystem:

    def __init__(self):
        self.students = []

    def add_student(self):
        roll_number = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")

        student = Student(roll_number, name)
        self.students.append(student)

        print(f"Student {name} added Successfully!")

    def mark_attendance(self):
        roll_number = int(input("Enter Student Roll Number: "))

        for student in self.students:

            if student.roll_number == roll_number:
                status = input(
                    "Enter Attendance Status (present/absent): "
                ).lower()

                student.mark_attendance(status)

                print(
                    f"Attendance marked for {student.name} as {status}."
                )

                return

        print("Student not found!")

    def view_attendance(self):
        roll_number = int(input("Enter Student Roll Number: "))

        for student in self.students:

            if student.roll_number == roll_number:
                student.display()
                return

        print("Student not found!")

    def calculate_percentage(self):
        roll_number = int(input("Enter Student Roll Number: "))

        for student in self.students:

            if student.roll_number == roll_number:
                percent = student.attendance_percentage()

                print(
                    f"Attendance Percentage for "
                    f"{student.name}: {percent:.2f}%"
                )

                return

        print("Student not found!")

    def display_student(self):

        if not self.students:
            print("No Students Record Found!")
            return

        print(
            f"\n{'RollNo.':<10}"
            f"{'Name':<15}"
            f"{'Attended Cls':<15}"
            f"{'Total Cls':<10}"
        )

        print("=" * 50)

        for student in self.students:
            student.display()


attendance = AttendanceSystem()


while True:

    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Calculate Percentage")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        attendance.add_student()

    elif choice == "2":
        attendance.mark_attendance()

    elif choice == "3":
        attendance.view_attendance()

    elif choice == "4":
        attendance.calculate_percentage()

    elif choice == "5":
        attendance.display_student()

    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
    
     


