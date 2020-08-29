# My list of things
spam = ['apples', 'bananas', 'tofu', 'cats']

def printTheList(someList):
    # Iterate through the list
    for item in range(len(someList)): 
        if item < len(someList)-2:
            component = ', '
        elif item == len(someList)-2:
            component = ' and '
        elif item == len(someList)-1:
            component = ' '
        print(someList[item] + component, end='')

# Call a function
printTheList(spam)
