# Change a string into a list
my_string = "MIT4Students"
L = list(my_string)
print(L)
L[3] = '3'
print(L)
new_string = ' '.join(L)
print(new_string)

for character in my_string:
    print(character)
print(my_string)