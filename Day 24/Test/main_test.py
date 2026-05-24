f = open("demofile.txt", "r")

print(f.readlines(33))  # The readlines command returns a list.

# Output is : It returns a list. The readlines command.
# ['Yohannes\n', 'is\n', '3\n', 'or 4']

# Part 2
# Replacing words un a string

txt = " I like Milk shakes"

x = txt.replace("Milk shakes" , "Fruits")
print(x)
# Python String strip() Method
#Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt2 = ",,,,,rrttgg.....banana....rrr"

x2 = txt.strip(",.grt")

print(x2)