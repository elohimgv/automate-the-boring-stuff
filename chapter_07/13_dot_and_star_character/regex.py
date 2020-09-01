
# Import module re
import re

# "." Matches any character except a newline

def atRegex():
    # Creating regex object
    regex = re.compile(r'.at')
    # Matching object
    mo = regex.findall("The cat in the hat sat on the flat mat.")
    print(mo)

# "*" Matches 0 or more (greedy) repetitions of the preceding RE
# .* Matching everything with dot and star

def nameRegex():
    # Creating regex object
    regex = re.compile(r'First name: (.*) Last name: (.*)')
    # Matching object
    mo = regex.findall("First name: Pedro Last name: Gutierrez")
    print(mo)

# "?" Match 0 or 1 of the preceding RE

def nonGreedyRegex():
    # Creating regex object
    regex = re.compile(r'<.*?>')
    # Matching object
    mo = regex.search("<To serve man> for dinner.>")
    print(mo.group())

def greedyRegex():
    # Creating regex object
    regex = re.compile(r'<.*>')
    # Matching object
    mo = regex.search("<To serve man> for dinner.>")
    print(mo.group())

# Matching newlines with dot character 

def noNewLineRegex():
    # Creating regex object
    regex = re.compile(r'.*')
    # Matching object
    txt = "Serve the public trust. \nProtect the innocnet. \nUpload the law."
    regex = regex.search(txt).group()
    print(regex)

# To accept new lines

def newLineRegex():
    # Creating regex object
    regex = re.compile('.*', re.DOTALL)
    # Matching object
    txt = "Serve the public trust. \nProtect the innocnet. \nUpload the law."
    regex = regex.search(txt).group()
    print(regex)

# Calling function
atRegex()
print()
nameRegex()
print()
nonGreedyRegex()
print()
greedyRegex()
print()
noNewLineRegex()
print()
newLineRegex()
