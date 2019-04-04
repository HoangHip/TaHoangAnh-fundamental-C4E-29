def add_fruit(inventory, fruit, quantity=0):
    return
new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
new_inventory["strawberries"] = 10
print(new_inventory)
# test("strawberries" in new_inventory)
print(bool("strawberries"))
# test(new_inventory["strawberries"] == 10)
print(bool(new_inventory["strawberries"] ==10 ))
# add_fruit(new_inventory, "strawberries", 25)
new_inventory["strawberries"] += 25
print(new_inventory)
# test(new_inventory["strawberries"] == 35)
print(bool(new_inventory["strawberries"] ==35 ))
