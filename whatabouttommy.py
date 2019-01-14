things_about_tommy = [
    "chompi",
    "burben",
    "marioKart",
    "sparkling water",
    "netflix",
    "yingling",
    "cleaning",
    "banana"
]

fte = [
    "lamb chomps",
    "lobster",
    "churassco",
    "broccoli",
    "all of jim's cooking",
    "fries",
    "nutella",
]

things_about_tommy.extend(fte)

count = 0

while count < 2:
    count += 1
    if count == 2:
        print("You got one more guess moron!")
    guess = input("\n\nWhat about Tommy: ")
    if guess.lower() in things_about_tommy:
        print("You Win!")
        exit(0)

print('You Lose Dummy')
