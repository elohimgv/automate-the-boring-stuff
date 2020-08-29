#! python3 

# To know where is the module 'pyperclip' from the PYTHONPATH. 
# PMSP (Python Module Search Path), invoke this:
# import sys
# for i in sys.path:
#    print(i)

import pyperclip 

pyperclip.copy('Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars')
# Variable to store text
text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n') 
for i in range(len(lines)): # loop through all index in the "lines" list
    lines[i] = '* ' + lines[i] # add a star to each string in "lines" list
# pyperclip.copy expect a string value not a list of values
text = '\n'.join(lines)
pyperclip.copy(text)

