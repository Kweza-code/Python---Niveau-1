

def contact():
    def menu():
        print("Please choose an action: ")
        print("1: Add a contact")
        print("2: Delete a contact")
        print("3: Show all the contact")
        print("0: Exit the app")

    actions = ["add", "delete", "showAll", "exit"]
    contactData = []

    while True:
        menu()
        action = int(input("Choose an action: "))
        if action == 0:
            print("Good Bye !")
            break

        if action in [1, 2, 3]:
            actionTaken = actions[action - 1]

            if actionTaken == "add":
                def phoneNumber(contactNumber):
                    number = 0
                    for char in contactNumber:
                        if char.isdigit():
                            number += 1

                    if number > 10:
                        return True
                    else:
                        return False

                while True:
                    contactNumber = (
                        input("Enter the phone number of your contact: "))

                    if phoneNumber(contactNumber):
                        break
                    else:
                        print("The phone number is not valid")

                contactName = input("Enter the name of your New contact :")

                contactListe = {
                    "contactName": contactName,
                    "contactNumber": contactNumber
                }

                contactData.append(contactListe)

                print(f"Welcome to {contactName}")

            elif actionTaken == "delete":

                if not contactData:
                    print("There is no contact to delete")
                    continue

                for index, item in enumerate(contactData):
                    print(f" {index + 1}: {item['contactName']}")

                deleteContact = int(
                    input("Please select the contact you want to delete ")) - 1
                if 0 <= deleteContact < len(contactData):
                    deleted = contactData.pop(deleteContact)
                    print(
                        f"You have deleted {deleted['contactName']}")

            elif actionTaken == "showAll":
                if contactData:
                    for index, item in enumerate(contactData):
                        print(f"{index + 1} {item['contactName']}")
                else:
                    print("You don't have contact yet")
                    continue


contact()
