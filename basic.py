############## Program demonstrating some basic code and functions ###############
print('AAlaikum')
print('What is your name : ')
yourName = input()	# input() function is used here
print('Welcome, ' + yourName + ' Its good to meet you ')
print('The length of your name is : ' + str(len(yourName))) 	# len() function is used to count number of characters in a string
print('Whats your age : ')
age = input()	# input() function always returns a string
print('You will be ' + str(int(age) + 1) + ' in a year')
MAX = 10	# MAX is a constant variable because its capitalized
i = 5
i = i + MAX
print('Value after adding constant variable to other variable becomes : %i' %i)	#	Observe printf() here


