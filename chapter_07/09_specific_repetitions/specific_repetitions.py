# Program name: specific_repetitions.py
#Import module re
import re

def fromMtoNrepetition(txt, m, n, q):
    """
    {m,n} match from m to n repetitions of preceding RE
    {m,n}? Non-greedy version of the above
    Examples of use:
    (str){3,5} match 'strstrstr', 'strstrstrstr', 'strstrstrstrstr'
    (str){3,} match three or more instances
    (str){,5} match zero to five instances
    """
    if q == '?':
         # Creating a regex object
        regex = re.compile(r'('+ txt +'){'+ str(m) +','+ str(n) +'}?')
    else:
         # Creating a regex object
        regex = re.compile(r'('+ txt +'){'+ str(m) +','+ str(n) +'}')

    # Matching object
    mo = regex.search("HaHaHaHaHaHa")
    # Return matching object
    print(mo.group())

# Calling a function
fromMtoNrepetition('Ha', 3, '', '')
