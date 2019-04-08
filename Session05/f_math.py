from random import randint,choice
from calculate import calc

x = randint(0, 9)
y = randint(0, 9)
list_op = ["+", "-", "*", "/" ]
op = choice(list_op)
if op == "/" and y == 0:
    op=choice(list_op)

result = calc(x, y, op)

error = choice([-1, 0, 0, 0, 0, 0, 0, 1])

result_1 = result + error
print("{0} {1} {2} = {3}".format(x, op, y, result_1))

answer_input = input("Y/N ? ").lower()

if result_1 == result:
    if answer_input == "y":
        print("bingo!")
    elif answer_input == "n":
        print("Wrong!!")
if result_1 != result:
    if answer_input == "n":
        print("bingo!")
    elif answer_input == "y":
        print("Wrong!!")

