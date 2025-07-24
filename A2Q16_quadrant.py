x=float(input("enter x co-ordinate"))
y=float(input("enter y co-ordinate"))
if(x==0.0 and y!=0):
      print("(",x,",",y,") is on the y-axis")
elif(y==0.0 and x!=0):
      print("(",x,",",y,") is on the x-axis")
else:
      if(x>0 and y>0):
            print("(",x,",",y,") is in quadrant I")
      elif(x>0 and y<0):
            print("(",x,",",y,") is in quadrant IV")
      elif(x<0 and y>0):
            print("(",x,",",y,") is in quadrant II")
      elif(x<0 and y<0):
            print("(",x,",",y,") is in quadrant III")
      else:
            print("(",x,",",y,") is in origin")
