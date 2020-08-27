# Program name: matching_regex_objects.py
# Import module re
import re 

# Creating regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d') # \d Match any decimal digit [0-9]
name = input("What's your name? ")
phone = input("What's your phone number? ")
# Matching object, string that will find
mo = phoneNumRegex.search(phone)
# Call match object group() to return the matching text string
print("The phone number of " + name + " is: " + mo.group())