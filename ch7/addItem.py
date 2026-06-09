def add_to_inventory(inventory,added_items):
    updated_inventory = inventory.copy()
    for item in added_items:
        updated_inventory.setdefault(item, 0)
        updated_inventory[item]+=1
    return updated_inventory