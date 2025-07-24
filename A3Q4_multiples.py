n=int(input("enter a no below which you want to find multiples: "))
s=0
for i in range (1,n,1):
      if(i%3==0 or i%5==0):
            s=s+i
print ("sum=",s)
