from random import choice
words = ["champion", "football", "hello"]
word = choice(words)
world_list = list(word)
shuffle_word = []

for i in range(len(word)):
    character = choice(world_list)
    shuffle_word.append(character)
    world_list.remove(character)
loop = True
while loop:
    print(*shuffle_word, sep=" ") # *: Xóa những kí tự linh tinh
    input_answer = input("Your answer: ")
    if input_answer == word:
        print("Hura")
        loop = False
    else:
        print("Wrong")