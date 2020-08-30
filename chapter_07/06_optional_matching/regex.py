# Import module re
import re

# "?" Matches 0  or 1 (greedy) of the preceding RE
planetRegex = re.compile(r'Satur(no)?na') # Creating regex object
# Matching object, string that will find
mo1 = planetRegex.search("Saturna is a name")
mo2 = planetRegex.search("Saturnona also is a name")
# Call match object with group() to return the matching text string
print("First matching object: " + mo1.group())
print("Second matching object: " + mo2.group())
