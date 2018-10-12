from random import randint #For generate random number

randnum = randint(1, 200)
print("Let's guess a number between 1 and 200!")
while True:
    guessnum = int(input("Tell me your guess:\t"))
    if guessnum > randnum:
        print("Enter a smaller number")
    elif randnum > guessnum:
        print("Enter a bigger number")
    else:
        print("You found it! The number was {0}".format(randnum))
        break
