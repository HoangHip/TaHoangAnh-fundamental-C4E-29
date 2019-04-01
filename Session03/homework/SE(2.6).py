flock_size = [5, 7, 300, 90, 24, 50, 75]
month=0
loop = True
print("Hello, my name is Hoang Anh and there are my sheep size")
print(flock_size)
print("Now my biggest sheep has size {} let's shear it ".format(max(flock_size)))
flock_size[flock_size.index(max(flock_size))]= 8
print("After shearing, here is my flock ")
print(flock_size)
your_months = int(input("Enter the number of months you want working as shepherd = "))
while loop:
    month +=1
    print("Month {} :".format(month))
    print("One month has passed, now here is my flock")
    for i in range(len(flock_size)):
        flock_size[i] += 50
    print(flock_size)
    if month < 3:
        print("Now my biggest sheep has size {} let's shear it ".format(max(flock_size)))
        flock_size[flock_size.index(max(flock_size))]= 8
        print("After shearing, here is my flock ")
        print(flock_size)
    elif month ==3:
        print("My flock has size in total:" ,sum(flock_size))
        x= sum(flock_size)*2
        loop = False
        print("I would get {} * 2$ = ".format(sum(flock_size)), x, "$")