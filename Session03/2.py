fav = ["Death note", "Netflix", "Teaching"]
print(*fav, sep=", ") 
input_fav = input("What's fav? ")
fav.append(input_fav)
for index, item in enumerate(fav):
    # print(index+1,item, sep=". ")
    print("{}. {}".format(index+1, item))
