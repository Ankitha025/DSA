class Stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
            
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peak from an empty stack")
            
    def size(self):
        return len(self.items)
    
stack=Stack()
print("Is the stack empty?",stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:",stack.items)
print("top of th stack:",stack.peak())
print("pop:",stack.pop())
print("stack after pop:",stack.items)
print("Is the stack empty?",stack.is_empty())
print("size of the stack:",stack.size())