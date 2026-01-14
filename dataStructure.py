'''Q. Data Structures: Implement a custom stack data 
structure with push, pop, and min operations, 
all in constant time.'''


class dataStruct:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self,x):
        self.stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        if not self.stack:
            raise IndexError("Stack underflow")
        self.min_stack.pop()
        return self.stack.pop()
    
    def min(self):
        if not self.min_stack:
            raise IndexError("Stack Underflow")
        return self.min_stack[-1]
    
    def top(self):
        if not self.stack:
            raise IndexError("Accessing top element from empty stack.")
        return self.stack[-1]
    

d=dataStruct()

#d.pop()
d.push(100)
d.push(12)
d.push(20)
d.push(30)

m=d.min()
print("min: ",m)
t=d.top()
print("top: ",t)
print("popped element: ",d.pop())

t=d.top()
print("top: ",t)
    