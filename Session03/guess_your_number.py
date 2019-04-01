from random import randint
n = randint(0,100)
low = 0
high = 100
loop = True
print('''Guess your number
       Now think your number from 1 to 100
       Let's start!
       ''') 
input()
while loop:
    mid = (low + high) // 2
    answer = input("Is {} your number? ".format(mid))   #{} là khoảng trống .format() : điền vào khoảng trống

    if answer == 'c' :
        loop = False
        print("Bingo")
    elif answer == 'l':
        high = mid
    elif answer == 's':
        low = mid
    
        
        
    



    