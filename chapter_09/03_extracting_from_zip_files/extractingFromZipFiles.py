# extractingFromZipFiles.py - Extracts all the files and folders
# from a ZIP file into the current working directory

import zipfile, os

# Move to the folder with example.zip
os.chdir('./Documents')
exampleZip = zipfile.ZipFile('example.zip')
#exampleZip.namelist()
#exampleZip.extract('spam.txt') # Match one of the strings in the list returned by namelist() 
exampleZip.extractall() # Extract all the files and folders
exampleZip.close()