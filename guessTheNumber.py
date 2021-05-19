#################	Guess the number program/game	###################
import random
secretNumber = random.randint(1, 12)
print('The number is I am thinking of is between 1 and 12')

# Ask the player to guess in 5 turns
for guessNumber in range(1, 6):
	print('Enter the guessed number')
	guess = int(input())

	if guess < secretNumber:
		print('Your guess is too low')
	elif guess > secretNumber:
		print('Your guess is too high')
	else:
		break	#  You guessed it correctly

if (guess == secretNumber):
	print('You guessed the number in ' + str(guessNumber) + ' turns !!!')
else:
	print('Sorry, the number I was thinking of was' + str(secretNumber))


