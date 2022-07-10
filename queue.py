class myqueue:
    def __init__(self):
        self.data=[]
    def length(self):
        return len(self.data)
    def enqueue(self,element):
        if len(self.data)<5:
            return self.data.append(element)
        else:
            return "overflow"
    def dequeue(self):
        if len(self.data)==0:
            return "underflow"
        else:
            self.data.pop(0)
b=myqueue()
b.enqueue(2)
b.enqueue(5)
b.enqueue(10)
b.enqueue(15)
print(b.data)
b.dequeue()#to remove the element that we have inserted in the queue
print(b.data)
