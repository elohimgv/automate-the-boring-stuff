# Program name: optional_matching.py
# Import module re
import re

# Creating a regex object
planetRegex = re.compile(r'Satur(no)?na') # Matches 0  or 1 of the preceding RE
# Matching object, string that will find
mo1 = planetRegex.search("Saturna is a name")
mo2 = planetRegex.search("Saturnona also is a name")
# Call match object grop() to return the matching text string
print("First matching object: " + mo1.group())
print("Second matching object: " + mo2.group())