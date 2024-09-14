height = float(input("Enter height:"))
weight = float(input("Enter weight"))
BMI = weight/(height/100)**2
print("Your BMI is :",BMI)
if BMI <=18.4:
    print("underweight")
elif BMI <=24.9:
    print("Healthy")
elif BMI <=34.9:
    print("over weight")
else:
    print("obese")