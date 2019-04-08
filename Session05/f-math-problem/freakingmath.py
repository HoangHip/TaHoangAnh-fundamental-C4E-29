from random import *
from calculate import calc
# làm cách nào để random ra các số 
def generate_quiz():
    x = randint(0, 9)
    y = randint(0, 9)
    list_op = ["+", "-", "*", "/" ]
    op = choice(list_op)
    if op == "/" and y == 0:
        op=choice(list_op)
    result = calc(x, y, op)

    error = choice([-1, 0, 0, 0, 0, 1])
    result = result + error
    # Hint: Return [x, y, op, result]
    return [x, y, op, result]
#check đáp án của người tl
def check_answer(x, y, op, result, user_choice):
    result_true = 0
    result_true = calc(x, y, op)    
    if result == result_true:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    elif result != result_true:
        if user_choice == False:
            return True
        elif user_choice == True:
            return False
    print(x," 1")
    print(y," 2")
    print(op," 3")
    print(result, " 4")
    print(user_choice, " 5")    

    # pass
    return True
# code ở file freakingmath -> chạy thử ở file app.py