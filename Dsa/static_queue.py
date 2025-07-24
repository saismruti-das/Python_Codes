def insert(q,item):
      global front,rear
      if rear==-1:
            front=rear=0
            q[rear]=item
      elif rear>=n-1:
            print("overflow")
      else:
            rear+=1
            q[rear]=item

def delete(q):
      global front
      if (front==-1 or front>rear):
            print("underflow")
      else:
            print('deleted item is',q[front])
            front+=1

def peek(q):
      if front==-1 or front>rear:
            print("queue empty")
      else:
            print("element at the front is",q[front])

def diaplay(q):
      if front==-1 or front>rear:
            print("queue empty")
      else:
            curr=front
            while(curr!=rear):
                  print(q[curr])
                  curr+=1
            print(q[curr])

front=rear=-1
n=int(input('no of elements'))
q=[0]*n
