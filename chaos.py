# File: Chaos.py
# A program to explain Chaotic behaviour

def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter any number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)

main()
