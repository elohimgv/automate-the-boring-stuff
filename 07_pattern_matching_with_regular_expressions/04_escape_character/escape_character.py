# Program name: escape_character.py
# Import module re
import re

# \(  \) to escape parentheses
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d-\d\d)') # Creating a regex object
# Matching object, string that will find
mo = phoneNumRegex.search("My cell phone numeber is (678) 789-90-90")
# Call match object with group() to return the matching text string
print(mo.group())
