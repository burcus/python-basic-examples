word = input("Enter a word:\t")
next = 1 #Like controller for move to the previous character
for character in word:
    if character != word[len(word) - next]: #e.g. "len(word)-1" gives us last character of input
        print("This word is not palindrom")
        exit()
    next+= 1
print("This word is palindrom!")
