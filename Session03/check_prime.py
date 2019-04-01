n = int(input("Enter your number : "))
i = 2
is_prime = True
# Cách 1:
if n == i:
    print("SNT")
while is_prime :    
    if n % i == 0:
        is_prime = False
        print("Khong phai SNT")
    i += 1
    if i == n:
        is_prime = False
        print("So NT")
# Kết luận

#  Cách 2:
# while i <n:
#     if n % i == 0:
#         is_prime = False
#     i += 1
# if is_prime == True:
#     print("La SNT")
# else:
#     print("KHONG PHAI SNT")
