# Program name: optional_matching.py
#Import module re
import re

string = "Remember we are working with REGEX"
print(string.upper())

# "+" Matches 1 or more repetitions of the preceding RE
plenetRegex = re.compile(r'Satur(na)+no') # Creating a regex object

while True:
    txt = input("What is the sixth planet on the solar sistem? ")
    # Call the search() method to find the pattern
    mo = plenetRegex.search(txt)
    # Call the match object group
    if txt == 'Saturno': # Cause an error...
        print("%r is the correct answer! XD" % mo.group())
    else:
        print("Although %r is no the correct answer is acceptable for 'Regex'" % mo.group())
        break





