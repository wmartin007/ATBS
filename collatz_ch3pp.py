# ATBS-Practice Projects-Chapter 3: Collatz Sequence

""" Write a function that accepts one parameter, number. If the number is
even, the function should print the number//2 and if it's odd it should print
3*number + 1"""


def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

def main():

    try:
        guess = int(input("Enter an integer:"))
        while guess != 1:
            guess = collatz(guess)
    except ValueError:
        print("Please enter an integer.")
        main()


main()