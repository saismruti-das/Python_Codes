num=int(input("enter a 3 digit no"))
temp=num
s=0
while(num!=0):
    d=num%10
    s=s+(d*d*d)
    num=num//10
if(temp==s):
    print ("armstrong number")
else:
    print("not armstrong no")
