class Stack:
    def __init__(self):
        self.stack = []
    def isempty(self):
        return(self.stack == [])
    def Push(self,v):
        self.stack.append(v)
    def Pop(self):
        v = None
        if not self.isempty():
            v = self.stack.pop()
        return v    
    def __str__(self):
        return(str(self.stack))
    

S = Stack()
S.Push(10)
S.Push(20)
S.Push(30)
S.Push(40)
print(S.Pop())
print(S.Pop())
print(S)