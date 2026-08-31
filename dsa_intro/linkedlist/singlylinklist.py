# Array size is fixed, but in python array size is dynamic.

# array-contiguous memory allocation
# singly linked list - non-contiguous memory allocation.

class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    def insertAtMid(self,value,x):
        temp=Node(value)
        t1=self.head

        while(t1.next != None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next

    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head != None):
            t1= self.head
            while(t1.next != None):
                t1=t1.next
            t1.next=temp
        else:
            self.head = temp
    
    def deleteLL(self,value):
        t1=self.head
        prev=t1
        if(t1.data ==value):
            self.head= t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next= t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next= None
    
    def printLL(self):
        t1= self.head
        while(t1.next != None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj=SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)