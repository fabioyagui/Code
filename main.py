# This is a sample Python script.
height = float(input("enter your height in cm: "))
weight = int(input("enter your weight in kg: "))
bmi = weight / (height/100) ** 2
bmi_as_int = int(bmi)



print(bmi_as_int)