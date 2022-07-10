class mystack:
    def __init__(self):
        self.data=[]
    def length(self):#length of the list
        return len(self.data)
    def is_full(self):#check if the list is full or not
        if len(self.data)==5:
            return True
        else:
            return False
    def push(self,element):#insert a new element
        if len(self.data)<5:
            self.data.append(element)
        else:
            return "overflow"
    def pop(self):#remove the last element from the list
        if len(self.data)==0:
            return "underflow"
        else:
            return self.data.pop()
        
a=mystack()#creating a stack
a.push(10)
a.push(15)
a.push(20)
a.push(25)
a.push(30)
print(a.length())
print(a.is_full())
print(a.data)
print(a.push(35))#trying to add one more element into the list 
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())#to try to delete an element in a list without elements