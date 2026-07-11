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

def reverse_string(s):
    stack = Stack(len(s))
    for char in s:
        stack.push(char)

    reversed_str = ""
    while not stack.isEmpty():
        reversed_str += stack.pop()
    return reversed_str

print(reverse_string("abc"))