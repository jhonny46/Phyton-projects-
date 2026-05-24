file=open('my_file.txt')
contents = file.read()
print(contents)
file.close()
# Or

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# To add a new line or content "W" to write
with open("my_file.txt", mode= "w") as file:
    file.write("\n Kebede is my grand fathers name ")

# if a file name does not exist it will create it for us.
with open("new_file.txt", mode= "w") as file:
    file.write("\n new text ")