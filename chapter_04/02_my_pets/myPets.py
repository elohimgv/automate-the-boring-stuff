# List of pets
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
# Interact with the console
name = input()
if name not in myPets:
    print("I do no have a pet named "+ name)
else:
    print(name + " is my pet.")
