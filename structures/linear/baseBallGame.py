class Solution(object):
    def calPoints(self, operations):
        class Stack:
            def __init__(self):
                self.stack = []
            
            def push(self, value):
                self.stack.append(value)
            
            def isEmpty(self):
                return len(self.stack) == 0
            
            def pop(self):
                if not self.isEmpty():
                    return self.stack.pop()
            
            def __str__(self):
                return str(self.stack)
            
            def sumAll(self):
                return sum(self.stack)
        
        s = Stack()
        for op in operations:
            if op == 'C':
                s.pop()
            elif op == 'D':
                if not s.isEmpty():
                    s.push(2 * s.stack[-1])
            elif op == '+':
                if len(s.stack) >= 2:
                    s.push(s.stack[-1] + s.stack[-2])
            else:
                s.push(int(op))
        
        return s.sumAll()
