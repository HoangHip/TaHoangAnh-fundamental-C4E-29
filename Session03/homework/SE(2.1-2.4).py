
flock_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hoang Anh and there are my sheep size")
print(flock_size)
input()
print("Now my biggest sheep has size {} let's shear it ".format(max(flock_size)))
flock_size[flock_size.index(max(flock_size))]= 8
input()
print("After shearing, here is my flock ")
print(flock_size)
input()
print("One month has passed, now here is my flock")
for i in range(len(flock_size)):
    flock_size[i] += 50
print(flock_size)
