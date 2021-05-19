# Program demonstrates use of functions in python
def hello(yourName):
    print('Assalam u Alaikum, ' + yourName)


print('Please Enter Your Name')
name = input()
hello(name)  # call to function hello(...)

#  Optional parameters for functions for example
#  print() has two optional parameters - end and sep
#  print something on separate lines
print('Hello')
print('Dear')
#  print on same line
print('Hello ', end='')  # newline is replaced by space
print('Dear')
#  print using comma separator
print('Hello ', 'Dear! ', 'How are you feeling today?')
#  replace default separating string using sep keyword
print('Blue', 'Black', 'White', 'Red', sep='$')  # words separated by $ symbol in output


#  Using global and local variables
def spam():
    global eggs  # this is a global variable defined somewhere out of this function
    eggs = 'spam'  # this is the global - updating its value


def bacon():
    eggs = 'bacon'  # this is a local variable
    print(eggs)


def ham():
    print(eggs)  # this is the global


eggs = 42  # this is the global variable - eggs
print(eggs)
spam()
ham()
bacon()
print(eggs)

# adding 10 spaces from beginning
print(' ' * 10, 'Warai chukh')  # adding 10 spaces from beginning
