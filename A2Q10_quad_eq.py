print("the exp is ax^2+bx+c=0")
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
d= b**2-4*a*c
if(d>0):
    r1= (-b +(d**(1/2)))/(2*a)
    r2= (-b -(d**(1/2)))/(2*a)
    print ("the two real roots are",r1,r2)
elif(d==0):
    r=-b/(2*a)
    print ("the real root is",r)
else:
    print ("there are no real roots")
