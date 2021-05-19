# Our Program is exploring Collatz Sequence also called "the simplest impossible math problem."
def collatz(number):
    #  Check whether the input number is even or odd
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1


try:
    while True:
        print("Please Enter any integer")
        num = int(input())
        num = collatz(num)
        if num == 1:
            print('Hurray!!! we got One')
            break
        else:
            print(num)
            continue

except ValueError:
    print('Sorry! you have entered a string instead of an integer.')
