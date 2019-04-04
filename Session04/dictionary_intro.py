person = {
    "name": "Duc",
    "age": 21,
    "university": ["FTU"],
    "gf-ex": 3

}

#tất cả thông tin trong {} là 1 dictionary.
#1 cặp thông tin bao gồm {key : value}

#1. READ
# print(person)
# print(person["name"])
# print(person["age"])

# loop by KEY
# for key in person.keys():
#     print(key)

# loop by value
for value in person.values():
    print(value)

# loop by item
# for key, value in person.items():
#     print(key, value)

# 2. CREATE or UPDATE

# person["gender"] = "unknown" #CREATE
# person["gf-ex"] = "5"        #UPDATE
# print(person)

# 3. DELETE

# del person["age"]
# print(person)


#Note: NUPDATE vào 1 list:
# uni = person["university"]
# uni.append("HNU")
# print(person)