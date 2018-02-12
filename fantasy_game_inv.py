from collections import Counter

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}




def displayInventory(inventory):
    print("Inventory:")
    for k, v in inv.items():
        print(str(v) + ' ' + k)

displayInventory(inv)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invToAdd = (Counter(dragonLoot))

for k, v in invToAdd.items():
    print(inv[k])
