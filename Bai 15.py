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

def sort_stack(stack):
    temp_stack = Stack(stack.capacity)
    
    while not stack.isEmpty():
        temp = stack.pop()
        while not temp_stack.isEmpty() and temp_stack.top() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    
    return stack

def print_stack(stack):
    temp = []
    while not stack.isEmpty():
        temp.append(stack.pop())
    for val in reversed(temp):
        print(val, end=' ')
        stack.push(val)
    print()

s = Stack()
s.push(3)
s.push(1)
s.push(2)
s.push(5)
s.push(4)

print("Before sorting:")
print_stack(s)

sort_stack(s)

print("After sorting (largest on top):")
print_stack(s)