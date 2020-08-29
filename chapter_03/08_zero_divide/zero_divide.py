# Program name: zero_divide.py

# Divide by cero cause and error
""""def spam(divideBy):
    return 42 / divideBy
print(spam(2))
print(spam(12))
print(spam(0)) # ERROR!
print(spam(1))"""

# Errors can be handled with 'try' and 'except' statements 
"""def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        # After running this code, the execution continues as normal 
        print('Error: Invalid argument.') 
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))"""

# Any error that occur in function calls in a try block will 
# be caught
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.') 
© 2020 GitHub, Inc.