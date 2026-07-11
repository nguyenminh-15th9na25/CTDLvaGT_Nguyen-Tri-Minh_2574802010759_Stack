class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
print(ms.getMin())
ms.push(2)
print(ms.getMin())
ms.pop()
print(ms.getMin())