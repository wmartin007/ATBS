# To display how arguments get passed to functions as references

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

"""Notice that when eggs is called, we don't have to assign it to a new
variable and print that variable. It modifies the list in place.    """