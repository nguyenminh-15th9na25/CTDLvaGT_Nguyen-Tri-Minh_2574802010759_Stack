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

def is_balanced(expression):
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.isEmpty():
                return False
            if stack.pop() != matching[char]:
                return False
    return stack.isEmpty()

print(is_balanced("([][])"))
print(is_balanced("([])"))
print(is_balanced("([)]"))
print(is_balanced("{[]}"))