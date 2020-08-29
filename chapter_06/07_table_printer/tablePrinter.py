#! python3 

# Data list
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bos', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

# Function
def printTable(table): 
    # A list of integers 
    colWidths = [0] * len(table)

    # Find the longest string in each of the inner list 
    for count in range(len(table)):
        for value in table[count]:
            if len(value) > colWidths[count]:
                colWidths[count] = len(value)

    # Estructuring the table    
    for data in range(len(table[0])):
        for index in range(len(table)):
            # Justify the text to right
            print(table[index][data].rjust(colWidths[index]), end=' ')
        print()

# Calling function
printTable(tableData)
