from random import *
word_list = ["meticulous", "champion", "hexagon"]
word = choice(word_list)
hint = list(word)
shuffle(hint)
print(*hint, sep=", ")
loop = True
while loop:
    answer = input("Your answer: ")
    if answer == word:
        print("Hura")
        loop = False
    else :
        print("Wrong")