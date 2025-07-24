def push(stk,item):
      global top
      if top>=n-1:
            print("overflow")
      else:
            top+=1
            stk[top]=item
      
def pop(stk):
      global top
      if top==-1:
            print("underflow")
      else:
            print("popped item is",stk[top])
            top-=1
            
def peek(stk):
      print("item on top is",stk[top])

def display(stk):
      curr=top
      while(curr!=-1):
            print(stk[curr])
            curr-=1

top=-1
n=int(input('no of elements'))
stk=[0]*n
