class node:
      def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

top=None

def push(data):
      global top
      n=node(data)
      if (top==None):
            top=n
      else:
            top.next=n
            n.prev=top
            top=n

def pop():
      global top
      if (top==None):
            print("underflow")
      else:
            print("popped element is",top.data)
            top=top.prev
            if (top):
                  top.next=None

def display():
      if(top==None):
            print("stack empty")
      else:
            curr=top
            while(curr):
                  print(curr.data)
                  curr=curr.prev
