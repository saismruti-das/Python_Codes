class node:
      def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

start=None

def insertbeg(data):
      global start
      n=node(data)
      if(start==None):
            start=n
      else:
            n.next=start
            start.prev=n
            start=n

def insertend(data):
      global start
      n=node(data)
      if(start==None):
            start=n
      else:
            curr=start
            while (curr.next):
                  curr=curr.next
            curr.next=n
            n.prev=curr


def countnodes():
      curr=start
      i=0
      while(curr):
            i+=1
            curr=curr.next
            
      return i
      
def insertpos(data,p):
      global start
      n=node(data)
      curr=prevn=start
      if p>countnodes()+1:
            print("Insertion not possible")
      elif start==None:
            start=n
      else:
            if p==1:
                  n.next=start
                  start.prevn=n
                  start=n
            else:
                  i=1
                  while i<p-1:
                        prevn=curr
                        curr=curr.next
                        i+=1
                  if(curr):
                        prevn.next=n
                        n.prev=prevn
                        n.next=curr
                        curr.prev=n
                  else:
                        prevn.next=n
                        
def found(elem):
      curr=start
      while(curr):
            if(curr.data==elem):
                  return True
            curr=curr.next
      return False

def insert_before_elem(data,elem):
      global start
      curr=prevn=start
      n=node(data)
      if found(elem):
            if start.data==elem:
                  n.next=start
                  start.prev=n
                  start=n
            else:
                  while(curr.data!=elem):
                        prevn=curr
                        curr=curr.next
                  prevn.next=n
                  n.prev=prevn
                  n.next=curr
                  curr.prev=n

def delbeg():
      global start
      if(start==None):
            print("list empty, cannot delete")
      elif start.next==None:
            start=None
      else:
            start=start.next
            start.prev=None

def delend():
      global start
      if(start==None):
            print("list empty, cannot delete")
      elif(start.next==None):
            start=None
      else:
            curr=start
            while(curr.next):
                  curr=curr.next
            prevn=curr.prev
            prevn.next=None

def delpos(p):
      global start
      if p>countnodes():
            print("cannot delete, as no node in given position")
      else:
            if p==1:
                  start=start.next
            else:
                  i=1
                  curr=start
                  while i<p:
                        curr=curr.next
                        i+=1
                  if (curr.next==None):
                        prevn=curr.prev
                        prevn.next=None
                  else:
                        prevn=curr.prev
                        curr=curr.next
                        prevn.next=curr
                        curr.prev=prevn
                        
def delelem(elem):
      global start
      if (found(elem)):
            if (start.data==elem):
                  start=start.next
            else:
                  curr=start
                  while(curr.data!=elem):
                        curr=curr.next
                  if (curr.next==None):
                        prevn=curr.prev
                        prevn.next=None
                  else:
                        prevn=curr.prev
                        curr=curr.next
                        prevn.next=curr
                        curr.prev=prevn
