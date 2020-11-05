# directoryTree.py - Rename every file in some folder and 
# also every file in every subfolder on that folder

import os

for folderName, subfolders, filenames in os.walk('/home/elohim/delicious'):
	print('The current folder is ' + folderName)


	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)


	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)


	print('')
