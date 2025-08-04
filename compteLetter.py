def compte():
    phrase = input("Enter a phrase : ")
    vowels = 0
    consonants = 0
    vowel = ["o", "a", "i", "e", "u"]

    for char in phrase.lower():  # convert to lowercase so it matches
        if char in vowel:
            vowels += 1
        elif char.isalpha():  # check it's a letter
            consonants += 1

    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)


compte()
