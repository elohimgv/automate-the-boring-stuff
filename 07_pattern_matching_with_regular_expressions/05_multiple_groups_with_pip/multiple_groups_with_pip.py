# Program name: multiple_groups_with_pip.py
# Import module re and random
import re
from random import choice 

# Creating a regex object
planetRegex = re.compile(r'Sat(urn|ori|o|iro)')
txt = ('urn', 'ori', 'o', 'iro')
slectText = choice(txt)
# Matching object, string that will find
mo = planetRegex.search('Sat' + slectText)
# Call match object group() to return the matching text string
print(mo.group())