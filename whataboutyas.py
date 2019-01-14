questions = {
    "what color hair? ": "blonde",
    "what color eyes? ": "blue",
    "how old? ": "25"
}

for question, answer in questions.items():
    count = 0
    while count < 3:
        guess = input(question)
        count += 1
        if guess.lower() == answer:
            print("you won")
            count = 3
        elif guess.lower() != answer and count < 3:
            print("you got " + str(3 - count) + " tries left")
        elif count == 3:
            print("you lose")
