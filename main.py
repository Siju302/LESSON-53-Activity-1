# write in file using with() function
with open('file.txt', 'w') as file:
    file.write("Hello...This is my first file in Python")
    file.write("\n")
    file.write("I am learnng file handling operations in Python")
file.close()

# split file into words
with open ('file.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()