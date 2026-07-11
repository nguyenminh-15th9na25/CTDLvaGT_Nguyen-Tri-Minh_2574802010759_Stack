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

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.top() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (not stack.isEmpty() and stack.top() != '(' and 
                   precedence.get(stack.top(), 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.push(char)
    
    while not stack.isEmpty():
        output.append(stack.pop())
    
    return ' '.join(output)

print(infix_to_postfix("a+b*c"))
print(infix_to_postfix("(a+b)*c"))
print(infix_to_postfix("a*b+c"))