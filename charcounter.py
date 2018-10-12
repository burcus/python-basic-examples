word = input("Enter a text\t")
letter = input("Which character are you looking for?\t")
counter = 0
for element in word:
    if element == letter:
        counter+=1
print("There are {0} -> {1}".format(counter,letter))
