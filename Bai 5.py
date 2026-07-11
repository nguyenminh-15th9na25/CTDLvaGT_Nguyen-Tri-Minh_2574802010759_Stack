class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow!")
            return
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow!")
            return None
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

def traverse_and_count(stack):
    temp_stack = Stack(stack.capacity)
    count = 0
    
    while not stack.isEmpty():
        temp_stack.push(stack.pop())
        count += 1
    
    elements = []
    while not temp_stack.isEmpty():
        val = temp_stack.pop()
        elements.append(val)
        stack.push(val)
    
    print(count)
    print(elements)
    return stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
traverse_and_count(s)