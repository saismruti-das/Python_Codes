d1=int(input("enter todays's day: "))
de=int(input("enter the number of days elapsed since today: "))
if (d1==0):
      dstr="Sunday"
elif (d1==1):
      dstr="Monday"
elif (d1==2):
      dstr="Tuesday"
elif (d1==3):
      dstr="Wednesday"
elif (d1==4):
      dstr="Thursday"
elif (d1==5):
      dstr="Friday"
elif (d1==6):
      dstr="Saturday"
else:
      print("invalid day")
d2=(d1+de)%7
if (d2==0):
      destr="Sunday"
elif (d2==1):
      destr="Monday"
elif (d2==2):
      destr="Tuesday"
elif (d2==3):
      destr="Wednesday"
elif (d2==4):
      destr="Thursday"
elif (d2==5):
      destr="Friday"
else:
      destr="Saturday"
print("Today is",dstr,"and the future day is",destr)

