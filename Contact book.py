class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email, address)
            print("Contact added successfully.")
    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts.values():
            print(contact)
    def search_contact(self, search_term):
        print("\nSearch Results:")
        for contact in self.contacts.values():
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            if address:
                self.contacts[name].address = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()