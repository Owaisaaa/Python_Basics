##############	While Loop ###############
while True:
	print('Whats your name : ')
	name = input()
	if name != 'owais':
		continue
	print("Hey! Owais. Tell me your password ")
	password = input()
	if password == 'lion':
		break
print("Access Granted! Welcome to the hunt.")
###############  for Loop ################
total = 0
for num in range(101):
	total = total + num
print(" The sum of numbers from 0 to 100 is : " + str(total))
#########  version 2  ##########
print("Second version of for loop")
for i in range(2, 8):
	print(i)
#########  version 3  ##########
print("3rd version of for loop")

for i in range(0, 10, 2):
	print(i)
#########  version 4  ##########
print("4th version of for loop")
for i in range(8, -2, -1):			# 3rd argument in range() function allows to run a loop in reverse order with one step
	print(i)	
################### import packages  ######################
import random
print('We can print random numbers between any two numbers say 1 and 10')
for i in range(6):
	print(random.randint(1,10))


