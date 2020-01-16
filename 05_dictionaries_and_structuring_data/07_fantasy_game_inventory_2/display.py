# Program name: display.py

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v 
        print(v, k)
    print("Total number of items: " + str(item_total))
