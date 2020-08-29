# List to cat names
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

# Print out all my cat names
print('The cat names are:')
# Loop to go through the list
for name in catNames:
    print('  ' + name)
