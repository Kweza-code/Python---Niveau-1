import json
import os

FILE_NAME = "todos.json"


def load_todos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_todos(todosList):
    with open(FILE_NAME, "w") as file:
        json.dump(todosList, file, indent=4)


def todo():
    print("Please enter a number :")
    print("1 : Add a todo")
    print("2: Delete a todo")
    print("3: See all the todos")
    print("4: Quite")

    action = ["add", "delete", "all", "quite"]
    todosList = load_todos()

    while True:

        try:
            choice_action = int(input("Chose a action: "))
            if choice_action == 0:
                print("Good bye")
                break

            if choice_action in [1, 2, 3, 4]:
                taken = action[choice_action - 1]

                if taken == "add":
                    newTodoName = input("Enter the name of the new todo")
                    newTodoDescription = input(
                        "Enter the description of your new todo")

                    todos = {
                        "newTodoName": newTodoName,
                        "newTodoDescription": newTodoDescription
                    }

                    todosList.append(todos)
                    save_todos(todosList)
                    print(f"New item added to your todos {newTodoName}")

                elif taken == "delete":
                    if not todosList:
                        print("There is nothing to delete ")
                        continue
                    print("Todos")

                    for index, item in enumerate(todosList):
                        print(
                            f"{index + 1}: {item['newTodoName'], {item['newTodoDescription']}}")

                    try:
                        test = int(
                            input("Chose which item you want to delete :")) - 1
                        if 0 <= test < len(todosList):
                            removed = todosList.pop(test)
                            save_todos(todosList)
                            print(f"You just delete {removed['newTodoName']}")
                        else:
                            print("Error")

                    except ValueError:
                        print("Error has occured")

                elif taken == "all":

                    for index, item in enumerate(todosList):
                        print(
                            f"{index + 1} : {item['newTodoName']} : {item['newTodoDescription']}")

        except ValueError:
            print("An error has occured")


todo()
