print('Enter your numbers one by one!\n')
print('Press "a" for to see average of numbers\n')
print('Press "q" for quit from program\n')
numCounter = 0
numTotal = 0
while True:
    userInput = input('Start enter your number or other option ( a / q )"\t')
    if userInput.isdigit() == True: #Working with Python3 because Python does not include isdigit() method
        numCounter += 1
        numTotal = numTotal + int(userInput)
    elif str(userInput) == 'a':
        print('Average of numbers:\t{}'.format(numTotal/numCounter))
        break
    elif str(userInput) ==  'q':
        print('Exiting...')
        exit()
