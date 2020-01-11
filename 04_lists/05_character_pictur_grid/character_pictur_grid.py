# Program name: character_pictur_grid.py

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

# Function to print the grid
def printTheGrid(y):
    for x in range(len(grid)):
        print(grid[x][y], end='')
        
    print()

printTheGrid(0)
printTheGrid(1)
printTheGrid(2)
printTheGrid(3)
printTheGrid(4)
printTheGrid(5)







            