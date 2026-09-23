
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError: # will run if there is no file error found in the try execution
    file = open("a_file.txt", "w")
    file.write("somthing")

except KeyError as error_message:   # runs if there's no error in the key, try execution
    print(f"Wrong Key {error_message} is inserted")

else:                           # runs if the try and accept our executed
    content = file.read() 
    print(content)

finally:                            # Is executed no matter the code succeed or fails
    file.close()
    print("The file is closed ")