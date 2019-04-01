fav = ["death note", "netflix", "teaching"]
print(*fav, sep=", ") # * để bỏ những dấu [] và '. sep=" ..." mỗi gt của list cách nhau 
input_fav = input("What's fav? ")
fav.append(input_fav)
print(*fav, sep=", ")

