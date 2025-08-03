

def temp():
    print("Enter 1 or 2 :")
    print("1: Convert Farenheint into Celcius")
    print("2: Convert Celcius into Farenheint")

    conv = ["C", "F"]

    while True:
        try:
            choice_number = int(input("Chose between 1 or 2 :"))
            if choice_number in [1, 2]:
                picked = conv[choice_number - 1]
                break

            else:
                print("Please enter a correct number")

        except ValueError:
            print("An error happened, please enter a number")

    temperature = int(input("Enter a degree: "))

    if picked == "C":
        celcius = (temperature - 32) * 5/9

        print(f"{temperature} Fahrenheit convert on Celcius is {celcius}")
    else:
        fahrenheit = (temperature * 9/5) + 32
        print(f"{temperature} Celcius convert on Fahrenheit is {fahrenheit}")


temp()
