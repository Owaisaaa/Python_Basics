############# Store birthday of friends in a dictionary ###############
birthDay = {'owais' : '28 July', 'zubair' : '31 May', 'JBaya' : '31 July', 'yamin' : '23 April'}
while True:
	print('Please Enter your name: (Blank to quit)')
	name = input()
	if name == ' ':
		break

	if name in birthDay:
		print(birthDay[name] + ' is the birthday of ' + name)
	else:
		print('No birthday information about ' + name)
		print('What is their birthday?')
		bDay = input()
		birthDay[name] = bDay
		print('birthdays database updated.')
