from random import shuffle
word = "champion"
hint = list(word)
shuffle(hint)
print(*hint, sep=", ")
loop = True
while loop:
    answer = input("Your answer: ")
    if answer == "champion":
        print("Hura")
        loop = False
    else :
        print("Wrong")
