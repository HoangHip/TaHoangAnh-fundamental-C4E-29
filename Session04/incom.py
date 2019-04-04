salary_table = [
    {
        "Name":"Hai",
        "Lương": 50000,
        "Ngày": 25,
        "Giờ/Ngày": 8
    },
    {
        "Name":"Duc",
        "Lương": 25000,
        "Ngày": 20,
        "Giờ/Ngày": 6,
    },
    {
        "Name":"Minh",
        "Lương": 20000,
        "Ngày": 27,
        "Giờ/Ngày": 5
    },
    {
        "Name":"Long",
        "Lương": 15000,
        "Ngày": 30,
        "Giờ/Ngày": 3
    },
    ]
# name_input = input("Nhập tên người cần tính lương: ")
# for person in salary_table:
#     if person["Name"] == name_input:
#         salary = person["Lương"]* person["Ngày"]* person["Giờ/Ngày"]
#         print(salary)
#         break
total_salary = 0
for person in salary_table:
    each_person = person["Lương"]* person["Ngày"]* person["Giờ/Ngày"]
    total_salary += each_person
print(total_salary)

