dict_days = {
    "Monday": "Thứ hai",
    "Tuesday": "Thứ ba",
    "Wednesday": "Thứ tư",
}
loop = True
while loop:
    for word in dict_days:
        print(word, end=', ') #\n = xuống dòng
    print()
    input_word = input("Code? ")
    if input_word in dict_days:
        mean = dict_days[input_word]
        print(mean)
    else:
        yes_or_no = input("Add word? (Y/N) ").lower() #upper() or lower()
        if yes_or_no == 'y':
            mean_input = input("Meaning? ")
            dict_days[input_word] = mean_input
        else:
            loop = False

