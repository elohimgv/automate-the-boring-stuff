# Program name comma_code.py

spam = ['apples', 'bananas', 'tofu', 'cats']

def things(list_of_things): 
    newType = list_of_things[0] + ', ' + list_of_things[1] + ', ' + list_of_things[2] + ', ' + 'and' + ', ' + list_of_things[3]
    return print(newType)

things(spam)