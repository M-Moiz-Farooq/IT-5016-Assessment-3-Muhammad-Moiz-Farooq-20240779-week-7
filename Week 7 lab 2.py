'''
week 7 lab 2 
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL
'''
class Student:
    def __init__(self):
        self.id = input("Enter your student id: ")
        self.last_name = input("Enter your last name: ")
        self.programme = input("Enter your programme (Diploma or Bachelors): ")
        print("Select One of the following options:")
        print("1. Withdrawal Of membership")
        print("2. Subscription Of membership")
        self.choice = input("Enter your choice: ")

class Membership:
    membership_id = 0
    members = []
    
    def __init__(self, student):
        self.student = student
       
    def new_membership(self):   
        if self.student.choice == "2":
            Membership.membership_id += 1
            print(f"Hi {self.student.last_name}, your membership ID is {Membership.membership_id}")
            Membership.members.append(self)
    def withdraw_membership(self):
        if self.student.choice == "1":
            print(f"Hi {self.student.last_name}, your membership has been withdrawn")
            if self in Membership.members:  # Check if the membership exists before removing
                Membership.members.remove(self)
    
def main():
    while True:
        student = Student()
        membership = Membership(student)
        if student.choice == "2":
            membership.new_membership()
        elif student.choice == "1":
            membership.withdraw_membership()
        response = input("Do you want to continue? (yes/no): ").lower()
        if response != 'yes':
            break

main() 
        
        
        
        
        
       
        
