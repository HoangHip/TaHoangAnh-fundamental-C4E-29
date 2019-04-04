answer = {
   "If x = 8, then what is the value of 4(x + 3) ?": [35, 36, 40, 44],
}
loop = True
print("Answer the following algebra question: ")

for key in answer.keys():
    print(key)
    for index, item in enumerate(answer[key]):
        print(index+1,".", item)
    while loop: 
        answer_input = input("Your choice: ")
        if answer_input == "4":
            print("Bingo")
            loop = False
        else:
            print(":(") 
