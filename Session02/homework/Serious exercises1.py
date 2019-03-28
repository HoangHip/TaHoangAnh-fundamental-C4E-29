height = int(input("Your height(CM):"))
weight = int(input("Your weight:"))
height1 =height/100
BMI=weight/(height1**2)
print("Your BMI: ", BMI)
if BMI < 16 :
    print("Severely underweight")
elif BMI< 18.5:
    print("Underweight")
elif BMI< 25:
    print("Normal")
elif BMI< 30:
    print("Overweight")
else:
    print("Obese")
