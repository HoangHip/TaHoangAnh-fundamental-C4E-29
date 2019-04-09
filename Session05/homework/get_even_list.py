def get_even_list(l):

    x=[]
    for index, item in enumerate(l):
        if item % 2 != 0:
            x.append(item)
    for item in x:
        l.remove(item)
    return l    
even_list = get_even_list([1, 2, 5, 9, -10, 6])
print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")    