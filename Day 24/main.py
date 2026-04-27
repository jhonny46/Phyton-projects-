file=open('my_file.txt')
contents = file.read()
print(contents)
file.close()
# Or

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# To add a new line or content
with open("my_file.txt", mode= "w") as file:
    file.write("\n Kebede is my grand fathers name ")