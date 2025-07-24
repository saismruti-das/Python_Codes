class node:
      def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

front=rear=None

def insert(data):
      global front,rear
      n=node(data)
      if(front==None):
            front=rear=n
      else:
            rear.next=n
            n.prev=rear
            rear=n

def delete():
      global front,rear
      if (front==None):
            print("underflow")
      elif(front.next==None):
            print("popped item is",front.data)
            front=rear=None
      else:
            print("popped item is",front.data)
            front=front.next
            front.prev=None

def display():
      if (front==None):
            print("underflow")
      else:
            curr=front
            while(curr):
                  print(curr.data)
                  curr=curr.next
      
      
