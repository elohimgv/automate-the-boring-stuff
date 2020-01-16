# Program name: fantasy_game_inventory_2.py

import display
# List
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Dict
inv = {'gold coin': 42, 'rope': 1}

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0) 
        for k, v in inventory.items():
            if k == i:
                inventory[i] = inventory[i] + 1 
    # Return new dictionary
    return inventory

# calling functions     
inv = addToInventory(inv, dragonLoot)
display.displayInventory(inv)
