# Program name: escape_character.py
# Import module re
import re

# Creating a regex object
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d-\d\d)') # \(  \) to escape parentheses
# Matching object, string that will find
mo = phoneNumRegex.search("My cell phone numeber is (678) 789-90-90")
# Call match object group() to return the matching text string
print(mo.group())