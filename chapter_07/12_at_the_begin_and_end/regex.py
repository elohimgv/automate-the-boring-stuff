# Import module re
import re

# "^" Matches the start of the string

def beginsWithHello():
    # Creating regex object
    regex = re.compile(r'^Hello') 
    # Matching object
    mo = regex.search("Hello World!")
    print(mo)
    print(mo.group())

# "$" Matches the end of the string or just 
# before the newline at the of the string

def endsWithNumber():
    # Creating regex object
    regex = re.compile(r'\d+$')
    # Matching object
    mo = regex.search("Your number is 42")
    print(mo)
    print(mo.group())

def wholeStringIsNum():
    # Creating regex object
    regex = re.compile(r'^\d+$')
    # Matching object
    mo = regex.search("0123456789")
    print(mo)
    print(mo.group())

# Calling function
beginsWithHello()
print()
endsWithNumber()
print()
wholeStringIsNum()
