class Whitecliffe:
    
    def __init__(self):
        self.studentID = input("Enter the Student ID: ")
        self.lname = input("Enter the last name of the student: ")
        self.program = input("Enter the program (Bachelor/Diploma): ")
        self.studentlist = []  # Stores students as tuples (lname, studentID, program)
        self.membershipcounter = 1000
        self.withdrawnstudentscounter = 400
        self.registeredstudentscounter = 600
        self.bachelorstudents = 500
        self.diplomastudents = 500

    def membership(self):
        # Add student to the student list
        self.studentlist.append((self.lname, self.studentID, self.program))
        self.membershipcounter += 1
        print(f"Hi {self.lname}, Your membership ID is: {self.membershipcounter}")
        
        # Increment the appropriate program count
        if self.program.lower() == "bachelor":
            self.bachelorstudents += 1
        elif self.program.lower() == "diploma":
            self.diplomastudents += 1
        else:
            print("Unknown program. No student added to Bachelor or Diploma counts.")

    def withdrawal(self):
        # Check if the student exists in the list, remove if found
        student = (self.lname, self.studentID, self.program)
        if student in self.studentlist:
            self.studentlist.remove(student)
            self.withdrawnstudentscounter += 1
            self.registeredstudentscounter -= 1
            print(f"Student {self.lname} has been withdrawn.")
        else:
            print("Student not found in the system.")
        
        # Update program count
        if self.program.lower() == "bachelor":
            self.bachelorstudents -= 1
        elif self.program.lower() == "diploma":
            self.diplomastudents -= 1

        # Show updated counts
        print(f"Registered Students: {self.registeredstudentscounter}")
        print(f"Withdrawn Students: {self.withdrawnstudentscounter}")

    def statistics(self):
        print(f"Number of registered students: {self.registeredstudentscounter}")
        print(f"Students in Diploma Program: {self.diplomastudents}")
        print(f"Students in Bachelor Program: {self.bachelorstudents}")
        print(f"Number of students who have withdrawn: {self.withdrawnstudentscounter}")


def main():
    system = Whitecliffe()
    while True:
        # Display the main menu
        choice = input("\n1. New Membership\n2. Withdraw Membership\n3. Statistics\n4. Exit\nChoose an option: ")
        
        if choice == "1":
            system.membership()
        elif choice == "2":
            system.withdrawal()
        elif choice == "3":
            system.statistics()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()