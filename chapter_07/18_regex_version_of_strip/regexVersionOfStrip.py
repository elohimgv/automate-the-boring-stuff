#! python3 

import re

# Regex version of strip()
def strip(text, space = ''):
    if space == 'l':
        # Regex object
        removeWhiteSpacefromBeginandEnd = re.compile(r'^\s+') 
        # Matching regex object to remove left whitespace
        return removeWhiteSpacefromBeginandEnd.sub('',text)
    elif space == 'r':
        # Regex object 
        removeWhiteSpacefromBeginandEnd = re.compile(r'\s+$') 
        # Matching regex object to remove right whitespace
        return removeWhiteSpacefromBeginandEnd.sub('',text)
    else:
        # Regex object
        removeWhiteSpacefromBeginandEnd = re.compile(r'^(\s+)(.*)(\s+)$') 
        # Matching regex object to remove whitespace from begin and end of string
        mo = removeWhiteSpacefromBeginandEnd.search(text)
        return mo.group(2)
    
# Call function
print(strip('     Hi Humberto! '))

