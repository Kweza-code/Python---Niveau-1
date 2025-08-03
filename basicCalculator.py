

def calculation():
    print("Picked your symbol")
    print("1: + ")
    print("2: - ")
    print("3: * ")
    print("4: / ")
    symbols = ["+", "-", "*", "/"]

    while True:
        try:
            choice_number = int(input("Enter 1, 2, 3 or 4 :"))
            if choice_number in [1, 2, 3, 4]:
                picked = symbols[choice_number - 1]
                print(f"You have choose {picked}")
                break
            else:
                print("The number is not valid, please enter 1, 2, 3 or 4")

        except ValueError:
            print("An Error happenend")

    number1 = int(input("Enter a number :"))
    number2 = int(input("Enter a second number :"))

    if picked == "+":
        result = number1 + number2
        print(result)
    elif picked == "-":
        result = number1 - number2
        print(result)
    elif picked == "*":
        result = number1 * number2
        print(result)
    else:
        result = number1 / number2
        print(result)


calculation()
