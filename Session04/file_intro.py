#1. CREAT file:
# myfile = open("alice_word.txt","w") #Tạo file .txt,"w" : lệnh viết thêm vào file
# myfile.write("Dcm kho vcl\n")
# myfile.write("----------------\n")
# myfile.write("lalalala")
# myfile.close()
#2. READ file:
#Cách 1 : Reading a file line-at-a-time
# mynewhandle = open("alice_word.txt","r")
# loop = True
# while loop:                             #Keep reading file forever
    # theline = mynewhandle.readline()    #Try to read next line
    # if len(theline) == 0:               #If there are no more lines 
        # loop = False                    # leave the loop
    #In ra những dòng vừa đọc
    # print(theline)
# mynewhandle.close()
#Turning a file into a list of lines
f = open("friends.txt", "r")
xs = f.readlines()
f.close()

xs.sort()

g = open("sortedfriends.txt", "w")
for v in xs:
    g.write(v)
g.close()