answer = [{
   "If x = 8, then what is the value of 4(x + 3) ?": [35, 36, 40, 44]
    },
    {
   "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52.What is the mean? ": ["About 55","About 65","About 75","About 85"]
    }]

print("Answer the following algebra question: ")
input_question = input("Do you want to add more question (Y/N) ").upper()
if input_question == "Y":
    question_add = input("Question: ")
    for
    answer_add = input("answer")
x = 0
for index, item in enumerate(answer):
    if index == 0:
        for key in item.keys():
            for index, item in enumerate(item[key]):
                print(index+1,".", item)
            answer_input = input("Your choice: ")
            if answer_input == "4":
                print("Bingo")
                x+=1
            else:
                print("Wrong!!")
    if index == 1:
        for key in item.keys():
            for index, item in enumerate(item[key]):
                print(index+1,".", item)
            answer_input = input("Your choice: ")
            if answer_input == "2":
                print("Bingo")
                x+=1
            else:
                print("Wrong!!")
print("you correctly answer {} out of 2 questions".format(x))
