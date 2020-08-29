# Program name comma_code.py

# My list of things
spam = ['apples', 'bananas', 'tofu', 'cats']

def printTheList(someList):
    for item in range(len(someList)): # Iterate through the list 
        if item < len(someList)-2:
            component = ', '
        elif item == len(someList)-2:
            component = ' and '
        elif item == len(someList)-1:
            component = ' '
        print(someList[item] + component, end='')

# Call a function
printTheList(spam)