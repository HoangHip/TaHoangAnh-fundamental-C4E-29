dictionary = {"hc": "học",
"eny": "em người yêu",
"nyc": "người yêu cũ",
}
loop = True
while loop:
    print("Welcome to dictionary")
    for key in dictionary.keys():
        print(key,end=7 * " ")
    print()
    word= input("Nhập từ bạn muốn dịch: ")
    if word in dictionary:
        print("*****************************************")
        print(dictionary[word])
    else:
        new_word = input("Bạn có muốn thêm từ này vào từ điển?(Y/N): ")
        if new_word == "Y":
            n = input("Nghĩa của từ này là: ")
            dictionary[word] = n
            print(dictionary)
        if new_word == "N":
            loop = False

