'''
Week 7 Lab 3
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL
'''

class RequestSystem():
    unique_id_counter = 1000  # Global unique ID counter

    def __init__(self):
        self.requests = []  # List to store all requests

    def user_info(self):
        """Collect basic user information."""
        name = input("Enter your name: ")
        return {"name": name}

    def request_details(self):
        """Collects item details and calculates total cost."""
        total_cost = 0
        items = []
        while True:
            item = input("Enter item name (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            cost = float(input(f"Enter cost for {item}: "))
            items.append({"item": item, "cost": cost})
            total_cost += cost
        return total_cost, items

    def generate_unique_id(self):
        """Generate a unique ID and increment the global counter."""
        unique_id = RequestSystem.unique_id_counter
        RequestSystem.unique_id_counter += 1
        return unique_id

    def generate_approval_ref(self, name, unique_id):
        """Generate an approval reference number based on the last 3 characters of the name and unique ID."""
        name_part = name[-3:] if len(name) >= 3 else name
        id_part = str(unique_id)[-3:]
        return f"{name_part}{id_part}"

    def request_approval(self, total_cost):
        """Approve if total cost < 150, else mark as pending."""
        return "approved" if total_cost < 150 else "pending"

    def submit_request(self):
        """Submit a new request."""
        user = self.user_info()
        total_cost, items = self.request_details()
        status = self.request_approval(total_cost)
        unique_id = self.generate_unique_id()
        approval_ref = self.generate_approval_ref(user["name"], unique_id)

        request = {
            "id": unique_id,
            "user": user,
            "items": items,
            "total": total_cost,
            "status": status,
            "approval_ref": approval_ref
        }
        self.requests.append(request)
        print(f"Request submitted with ID {unique_id} and status '{status}'.")
        print(f"Approval reference number: {approval_ref}")

    def display_requests_neatly(self):
        """Prints all the requests neatly with headers."""
        print("\n============================")
        print("        All Requests        ")
        print("============================")
        if not self.requests:
            print("No requests have been submitted yet.")
        else:
            print(f"{'ID':<5} {'Name':<15} {'Total Cost':<12} {'Status':<10} {'Approval Ref':<15}")
            print("-" * 60)
            for req in self.requests:
                print(f"{req['id']:<5} {req['user']['name']:<15} ${req['total']:<12.2f} {req['status']:<10} {req['approval_ref']:<15}")
            print("============================")

    def display_request_details(self, request_id):
        """Prints the details of a specific request."""
        for req in self.requests:
            if req['id'] == request_id:
                print("\n============================")
                print("        Request Details        ")
                print("============================")
                print(f"ID: {req['id']}")
                print(f"Name: {req['user']['name']}")
                print("Items:")
                for item in req['items']:
                    print(f"- {item['item']}: ${item['cost']:.2f}")
                print(f"Total Cost: ${req['total']:.2f}")
                print(f"Status: {req['status']}")
                print(f"Approval Ref: {req['approval_ref']}")
                print("============================")
                return
        print("Request not found.")

# Main program
def main():
    system = RequestSystem()

    while True:
        choice = input("\n1. Submit Request\n2. Display Requests\n3. Display Request Details\n4. Exit\nChoose an option: ")
        if choice == "1":
            system.submit_request()
        elif choice == "2":
            system.display_requests_neatly()
        elif choice == "3":
            request_id = int(input("Enter the request ID: "))
            system.display_request_details(request_id)
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()