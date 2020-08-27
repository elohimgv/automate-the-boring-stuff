# Program name: grouping_with_parentheses.py
# Import module re
import re

# Creating regex object
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d-\d\d)')
name = input("What's your name? ")
phone = input("What's your phone number? ")
# Matching object, string that will find
mo = phoneNumRegex.search(phone)
# Call match object group() to return the matching text string
print("First group: %r" % mo.group(1))
print("Second group: %r" % mo.group(2))