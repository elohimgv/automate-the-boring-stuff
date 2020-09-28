#! python3
# regexSearch.py - Find a string given by the user

import os, re

myFiles = ['extending_the_multiclipboard.txt','mad_libs.txt','regex_search.txt']
pattern = input('What word do you looking for? ') 
regex = re.compile(pattern)

for fileName in myFiles:
    # Relative path
    path = os.path.join('.', 'practice_projects', fileName)
    objectFile = open(path)
    content = objectFile.read()
    for search in content:
        mo = regex.search(content)
        if mo:
            print('Found ' + '"' + mo.group() + '"' + ' in ' + fileName)
            break
        else:
            print('Not found ' + '"' + pattern + '"' + ' in ' + fileName)
            break
    objectFile.close()