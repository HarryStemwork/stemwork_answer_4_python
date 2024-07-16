#BMI = kg / m2

weight = int(input("weight: "))
height = int(input("height (in m): "))

BMI = weight / height ** 2

if BMI < 18:
    print("Underweight")
elif BMI < 24:
    print("Normal")
else:
    print("Overweight")
