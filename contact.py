import json
import os

FILE_NAME = "ok.json"


def load():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    else:
        return []


contactList = load()


def saveContact():
    with open(FILE_NAME, "w") as file:
        json.dump(contactList, file, indent=4)


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
                def phoneNumber():
                    digit_count = sum(char.isdigit() for char in contactNumber)
                    has_letter = any(char.isalpha() for char in contactNumber)

                    if digit_count > 10 and not has_letter:
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

                print("Do you want to enter the email of your new contact ?")
                print("1: yes")
                print("2: no")

                answer = int(input("?"))

                if answer == 1:
                    contactEmail = input("Enter the email")
                else:
                    contactEmail = "No email register for this contact"

                contactListe = {
                    "contactName": contactName,
                    "contactNumber": contactNumber,
                    "contactEmail": contactEmail

                }

                contactData.append(contactListe)

                # Save only the newly added contact immediately
                with open('read.txt', 'a') as file:
                    json.dump(contactListe, file)
                    file.write("\n")

                print(f"Welcome to {contactName}")

            elif actionTaken == "delete":

                if not contactData:
                    print("There is no contact to delete")
                    continue

                for index, item in enumerate(contactData):
                    print(f" {index + 1}: {item['contactName']}")

                deleteContact = int(
                    input("Please select the contact you want to delete ")) - 1

                for contact

            elif actionTaken == "showAll":
                if contactData:
                    for index, item in enumerate(contactData):
                        print(f"{index + 1} {item['contactName']}")
                else:
                    print("You don't have contact yet")
                    continue


contact()
