n = int(input("Please enter your number : "))




# Cách 1:
# count_digit = 0
# while n > 0 :
#     n = n // 10
#     count_digit += 1
# print (count_digit)


# Cách 2:(Highly Recommend)
count_digit = 0
loop = True
while loop :
    n = n // 10
    count_digit += 1
    if n ==0:
        loop = False
print (count_digit)
