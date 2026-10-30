contacts ={}
def add_contact (contacts):
    name=input("enter contact name:")
    phone=input("enter phone number:")
    contacts[name]=phone
    print("contact added successfully!")
    return contacts
def search_contact(contacts):
    name=input("enter name to search:")
    if name in contacts:
        print("name:",name)
        print("phone:",contacts[name])
    else:
            print("contact not found")
def update_contact(contacts):
    name=input("enter name to update:")
    if name in contacts:
        phone=input("enter new phone number:")
        contacts[name]=phone
        print("contact updated successfully!")
    else:
            print("contact not found")
def delete_contact(contacts):
    name =input("enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("contact deleted successfully!")
    else:
            print("contact not found")
def view_contact(contacts):
    if contacts:
        print("\n saved contacts:")
        for name,phone in contacts.items():
            print(name,":",phone)
    else:
            print("no contacts available")
def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        search_contact(contacts)
    elif choice == "3":
        update_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        view_contacts(contacts)
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")
    
