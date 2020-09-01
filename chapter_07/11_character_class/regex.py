# Import module re
import re

# \d any numeric digit from 0 to 9
# "+" matches 0 or more (greedy) repetitions of the preceding RE
# \s Any spac, tab or newline character
# \w Any letter, numeric digit, or the underscore character

def xmasRegex():
    # Creating regex object
    regex = re.compile(r'\d+\s\w+')  
    txt = """12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 
    6 geese, 5 rings, 4 birds, 3 hens, 2 dives, 1 partridge"""
    # Matching object 
    mo = regex.findall(txt)
    print(mo)

# [ ] Indicates a set of characters 
# A "^" as the first character indicates a complementing set 

def vowelRegex():
    # Creating regex object
    regex = re.compile(r'[aeiouAEIOU]')
    # Matching object
    mo = regex.findall('The BEear eats a hoRSe')
    print(mo)

def consonantRegex():
    # "^" negative character class
    regex = re.compile(r'[^aeiouAEIOU]') # Creating regex object
    # Matching object
    mo = regex.findall('The BEear eats a hoRSe')
    print(mo)

# Calling fuctions
consonantRegex()
vowelRegex()
xmasRegex()

