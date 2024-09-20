import os

CONTACT_FILE = 'contacts.txt'

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    return []

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACT_FILE, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts List:")
    for idx, contact in enumerate(contacts):
        print(f"{idx + 1}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def edit_contact(contacts):
    """Edit an existing contact."""
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter the new name: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            contacts[index] = [name, phone, email]
            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    """Delete a contact."""
    view_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
