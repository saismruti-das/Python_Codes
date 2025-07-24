num=int(input("enter a no between 100 and 999: "))
temp=num
s=0
while(num!=0):
    d=num%10
    s=s+d
    num=num//10
print("the sum of the digits of",temp,"is",s)
