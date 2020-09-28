#! python3
# madLib.py - Write new text from input user in .txt file
# replacing the keywords ['ADJECTIVE','NOUN','VERB','NOUN']

# Input user
adjective = input('Enter an adjetive:\n')
noun1 = input('Enter a noun:\n')
verb = input('Enter a verb:\n')
noun2 = input('Enter a noun:\n')

# Lists
inputTexts = [adjective,noun1,verb,noun2]
searchText = ['ADJECTIVE','NOUN','VERB','NOUN']

# Function
def writeNewText(inputText, searchText):
    appearances = 0

    objectFile = open('madlib.txt')
    # To obtain a type str()
    content = objectFile.read()
    objectFile.close() 

    objectFile = open('madlib.txt', 'w')
    for start in range(len(content)):
        for stop in range(len(content)):
            if content[start:stop] == searchText:
                # Count appearances
                appearances = appearances + 1
                if appearances > 1:
                    break
                else:
                    objectFile.write(content[0:start] + inputText + content[stop:])
                    break
    objectFile.close()

# Calling function
for i in range(len(inputTexts)):    
    writeNewText(inputTexts[i], searchText[i])


