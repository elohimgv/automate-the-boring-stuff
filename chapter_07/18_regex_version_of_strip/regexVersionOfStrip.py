#! python3 

import re

# Regex version of strip()
def strip(text, space = ''):
    if space == 'l':
        # Regex object
        removeWhiteSpacefromLeft = re.compile(r'^\s+') 
        # Matching regex object to remove left whitespace
        return removeWhiteSpacefromLeft.sub('',text)
    elif space == 'r':
        # Regex object 
        removeWhiteSpacefromRight = re.compile(r'\s+$') 
        # Matching regex object to remove right whitespace
        return removeWhiteSpacefromRight.sub('',text)
    else:
        # Regex object
        removeWhiteSpacefromLeftandRight = re.compile(r'^(\s+)(.*)(\s+)$') 
        # Matching regex object to remove whitespace from begin and end of string
        mo = removeWhiteSpacefromLeftandRight.search(text)
        return mo.group(2)
    
# Call function
print(strip('     Hi Humberto! '))

