from random import randint #For generate random number

randNum = randint(1, 200)
print("Let's guess a number between 1 and 200!")
while True:
    guessNum = int(input("Tell me your guess:\t"))
    if guessNum > randNum:
        print("Enter a smaller number")
    elif randNum > guessNum:
        print("Enter a bigger number")
    else:
        print("You found it! The number was {0}".format(randNum))
        break
