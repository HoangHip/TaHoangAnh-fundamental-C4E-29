from random import randint
n = randint(0,100)

# from random (Highly recommend khi sử dụng nhiều thư viện có cùng chức năng e.i= turtle,random,..)   
# n = random.randint(0,100)
loop = True
while loop:
    player_number = int(input("Your Number: "))
    if player_number > n:
        print("too large")
    elif player_number < n:
        print("too small")
    else:
        print("Bingo")
        loop = False
    


    