list_items = ['T-shirt','Sweater']
loop = True
while loop:
    x = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if x == "R":
        print(*list_items, sep =", ")
    elif x == "C":
        new_item = input("Enter new item: ")
        list_items.append(new_item)
        print(*list_items, sep =", ")    
    elif x == "U":
        update = int(input("Update position? (0-{}) ".format(len(list_items)-1)))
        new_item = input("New item ? ")
        list_items[update]=(new_item)
        print(*list_items, sep =", ")
    elif x == "D":
        delete_item = int(input("Delete position? (1-{}) ".format(len(list_items))))
        delete_item -= 1
        del list_items[delete_item]
        print(*list_items, sep =", ")
    elif x== "end":
        loop = False
        print("End program!!")
    else:
        print("Wrong command! Please use (C, R, U, D) or 'end' to end the program")
        
        
    
