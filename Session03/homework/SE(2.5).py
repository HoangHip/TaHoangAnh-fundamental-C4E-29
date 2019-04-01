n = 0
loop = True
flock_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hoang Anh and there are my sheep size")
print(flock_size)
x= int(input("Enter the number of months to caculate = "))
while loop:
    n +=1
    print("Month {} :".format(n))     ,   
    print("One month has passed, now here is my flock")
    for i in range(len(flock_size)):
        flock_size[i] += 50
    print(flock_size)
    print("Now my biggest sheep has size {} let's shear it ".format(max(flock_size)))
    flock_size[flock_size.index(max(flock_size))]= 8
    print("After shearing, here is my flock ")
    print(flock_size)
    print()
    if n == x:
        loop = False