import json
import os

FILE_NAME = "contact.json"

# Load contacts from file


def load():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file


def save():
    with open(FILE_NAME, "w") as file:
        json.dump(contactList, file, indent=4)

# Display menu options


def show_menu():
    print("\nPlease choose an option:")
    print("1: Add a contact")
    print("2: View all contacts")
    print("3: Delete a contact")
    print("0: Exit")


# Load existing contacts
contactList = load()

# Main program loop


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break

        elif choice == 1:
            contact_name = input("Enter the name of the new contact: ")
            contact_bio = input("Enter the bio of the new contact: ")
            contact = {
                "contactName": contact_name,
                "contactBio": contact_bio
            }
            contactList.append(contact)
            save()
            print(f"New contact '{contact_name}' saved.")

        elif choice == 2:
            if not contactList:
                print("No contacts found.")
            else:
                print("Your contacts:")
                for contact in contactList:
                    print(
                        f"- {contact['contactName']}: {contact['contactBio']}")

        elif choice == 3:
            contact_name = input("Enter the name of the contact to delete: ")
            found = False
            for contact in contactList:
                if contact["contactName"] == contact_name:
                    contactList.remove(contact)
                    save()
                    print(f"Contact '{contact_name}' deleted.")
                    found = True
                    break
            if not found:
                print("Contact not found. Please try again.")

        else:
            print("Invalid option. Please choose a valid number.")


# Run the program
main()
