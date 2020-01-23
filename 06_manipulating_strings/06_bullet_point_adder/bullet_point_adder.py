#! /usr/bin/python 
# bullet_point_adder.py - Adds Wikipedia bullet point 
# to the start of each line of text on the clipboard.

# Revising where is the module 'pyperclip' from the PYTHONPATH. 
# To know the PMSP (Python Module Search Path), invoke this:
# import sys
# for i in sys.path:
#    print(i)
import pyperclip 

# Variable to store text; using method paste() 
# from module pyperclip 
text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n') 
for i in range(len(lines)): # loop through all index in the "lines" list
    lines[i] = '* ' + lines[i] # add a star to each string in "lines" list
# pyperclip.copy expect a string value not a list of values
text = '\n'.join(lines)
pyperclip.copy(text)

