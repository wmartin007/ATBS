# Exception Handdling in Python

# def spam(divideBy):
#     return 42 / divideBy

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(2))
print(spam(12))
print(spam(0)) # Without using try and except, this line will throw
# an error and prevent the rest of the script from running.
print(spam(1))
