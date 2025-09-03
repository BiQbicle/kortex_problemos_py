class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    
    try:
        with open("contacts.txt", "a") as file:
            file.write(f"{name},{phone},{email}\n")
        print("Contact added!")
    except:
        print("Error saving contact")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No contacts found")
                return
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    print(f"{parts[0]} - {parts[1]} - {parts[2]}")
    except FileNotFoundError:
        print("No contacts found")
        
def search_contact():
    search_variable = input("Enter the name of the contact: ")
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No contacts found")
                return
            for line in lines:
                
                parts = line.strip().split(",")
                if len(parts) >= 3 and parts[0] == search_variable:
                    print(f"{parts[0]} - {parts[1]} - {parts[2]}")
    except FileNotFoundError:
        print("No contacts found")
    

while True:
    print("\n1. Add Contact")
    print("2. View Contacts") 
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Pick a number: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Try again")