time = int(input("what time is it now? "))
am_pm = input("am/pm ").lower()
hours_wait = int(input("Please enter the number of hours to wait: "))
alarm = hours_wait % 24 + time
# print(alarm)
if am_pm == "am":    
    if alarm > 12:
        alarm = alarm - 12
        print("It is {} pm now".format(alarm))
    else:
        print("It is {} am now".format(alarm))
elif am_pm == "pm":
    if alarm > 12:
        alarm = alarm - 12
        print("It is {} am now".format(alarm))
    else:
        print("It is {} pm now".format(alarm))
    
 