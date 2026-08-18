# QUEUE AND DEQUEUE
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is empty")
        else :
            return self.items.pop(0)
    
    def insertAtFront(self,value):
        self.items.insert(0,value)
    
    def deleteAtEnd(self):
        self.itmes.pop()

q= Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())