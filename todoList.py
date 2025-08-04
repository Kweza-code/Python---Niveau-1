def todo():

    action_choices = ["add", "delete", "all"]
    todoAll = []
    print("Veuillez choisir les options")
    print("1 : Ajouter un todo")
    print("2: Supprimer un todo")
    print("3: afficher tous les todos")
    print("0 : Quitter")

    while True:
        try:
            choice_number = int(input("Enter a number "))
            if choice_number == 0:
                print("Good bye")
                break

            if choice_number in [1, 2, 3]:
                action = action_choices[choice_number - 1]
                print(f"you have picked {action}")

                if action == "add":
                    name = input("Enter the name of your todo: ")
                    description = input("Enter the description of your todo: ")

                    todos = {
                        "name": name,
                        "description": description
                    }

                    todoAll.append(todos)
                    print(
                        f"New todo : name : {name}, description : {description}")

                elif action == "delete":
                    if not todoAll:
                        print("Nothing to delete in your todoList")
                        continue

                    print("Todos :")
                    for index, item in enumerate(todoAll):
                        print(
                            f"{index + 1}:  {item['name']} - {item['description']}")

                    try:
                        index_to_delete = int(
                            input("Enter the number of the todo to delete: ")) - 1
                        if 0 <= index_to_delete < len(todoAll):
                            removed = todoAll.pop(index_to_delete)
                            print(f"Removed todo: {removed['name']}")
                        else:
                            print("Invalid index.")
                    except ValueError:
                        print("Please enter a valid number.")

                elif action == "all":
                    if not todoAll:
                        print("No todos yet.")
                    else:
                        print("Your todos:")
                        for index, item in enumerate(todoAll):
                            print(
                                f"{index + 1}:  {item['name']} - {item['description']}")
            else:
                print("Please enter a correct action number")

        except ValueError:
            print("An error occurred ")


todo()
