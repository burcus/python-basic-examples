ourFile = open("testfile.txt","w+")
ourFile.write("Let's add something to the file\n")
ourFile.write("This will be our second line\n")
ourFile.write("write method does not add enter")
ourFile.seek(0) #If you don't write that you can only see empty line. This will take us to file's beginning
print(ourFile.read())