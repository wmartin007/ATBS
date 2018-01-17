spam = ['apples', 'bananas', 'tofu', 'cats']
oneword = ['apples']
empty = []
def commaCode(list):
    string = ''
    if len(list) == 1:
        return list[0]
    else:
        for i, word in enumerate(list):
            if i < len(list) - 1:
                string += word + ", "
            elif i == len(list) - 1:
                string += "and " + word
        return string

print(commaCode(spam))
print(commaCode(oneword))
print(commaCode(empty))