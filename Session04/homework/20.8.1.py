diction ={}
str_input = input().lower()
characterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in characterlist:
    diction[i]= str_input.count(i)
    if diction[i]==0:
        del diction[i]

for key in diction.keys():
    print(key, diction[key])