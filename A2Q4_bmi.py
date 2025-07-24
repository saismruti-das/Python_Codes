w=float(input("enter weight in pounds: "))
h=int(input("enter ht in inches: "))
wkg=w*0.45359237
hm=h*0.0254
bmi=wkg/(hm**2)
print("your bmi is",bmi)
