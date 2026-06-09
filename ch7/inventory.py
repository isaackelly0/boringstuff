def display_inventory(inv):
    print('Inventory:')
    count = 0
    for k,v in inv.items():
        print(v, k)
        count+=v
    print('Total number of items: '+ str(count))
display_inventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} )