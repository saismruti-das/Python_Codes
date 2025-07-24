class node:                         #creation of node
      def __init__(self,data):
            self.data=data
            self.next=None
start=None

def insertbeg(data):
      global start
      n=node(data)
      if(start==None):              #empty list
            start=n
            n.next=start
      else:
            curr=start
            while(curr.next!=start):
                  curr=curr.next
            n.next=start
            start=n
            curr.next=start

def insertend(data):
      global start
      n=node(data)
      if(start==None):              #empty list
            start=n
            n.next=start
      else:
            curr=start
            while(curr.next!=start):
                  curr=curr.next
            curr.next=n
            n.next=start

def delbeg():
      global start
      if (start==None):             #check for empty list
            print("list empty, cannot delete")
      elif(start.next==start):      #check for single node
            start=None
      else:
            curr=start
            while(curr.next!=start):
                  curr=curr.next
            start=start.next
            curr.next=start

def delend():
      global start
      if (start==None):             #check for empty list
            print("list empty, cannot delete")
      elif(start.next==start):      #check for single node
            start=None
      else:
            curr=start                          #prev=curr=start
            while(curr.next.next!=start):       #while(curr.next!=start):
                  curr=curr.next                      #prev=curr
            curr.next=start                           #curr=curr.next
                                                #prev.next=start

def traversal():
      if(start==None):
            print('empty list')
      else:
            curr=start
            while(curr.next!=start):
                  print(curr.data)
                  curr=curr.next
            print(curr.data)
