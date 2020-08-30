# Import module re and random
import re
from random import choice 

# A|B, creates an RE that will match either A or B
planetRegex = re.compile(r'Sat(urn|ori|o|iro)') # Creating regex object
txt = ('urn', 'ori', 'o', 'iro')
slectText = choice(txt)
# Matching object, string that will find
mo = planetRegex.search('Sat' + slectText)
# Call match object with group() to return the matching text string
print(mo.group())
