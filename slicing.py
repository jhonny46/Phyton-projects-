piano_keys = ["a", "b","c","d","e","f","g"]
piano_tupple = ("do", "re", "mi","fa", "so", "la", "ti")

print(piano_keys[2:5]) # Prints c d e
print(piano_keys[:5]) # Prints from a to e
print(piano_keys[2:5:2]) # prints c skips d and prints e\

#['c', 'd', 'e']
#['a', 'b', 'c', 'd', 'e']
#['c', 'e']

# To get everything in a list but only the second ithem.

print(piano_keys[::2]) #['a', 'c', 'e', 'g']
# Increments by 1 but from the last to first
print(piano_keys[::-1]) #['g', 'f', 'e', 'd', 'c', 'b', 'a']

print(piano_tupple[2:5])#('mi', 'fa', 'so')
print(piano_tupple[1:])