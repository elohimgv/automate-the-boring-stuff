# readingZipFiles.py - Read the content of zip file

import zipfile, os

# Move to the folder with example.zip
os.chdir('./Documets') 
# A ZipFile object
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist()) 
# Return a list for all the files and folders contained
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()