inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# Add a key to inventory called 'pocket'
inventory['pocket'] = ''
# Set the value of 'pocket' to be list consiting of the strings
inventory['pocket'] = list(inventory['pocket'])
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(*inventory['pocket'], sep= ", ")
# Then .remove('dagger') from backpack
inventory['backpack'].remove('dagger')
print(*inventory['backpack'],sep=" ,")
# Add 50 to 'gold' key
inventory['gold'] += 50
print(inventory['gold'])