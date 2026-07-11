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

def evaluate_rpn(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.push(result)
        else:
            stack.push(float(token))
    return stack.pop()

print(evaluate_rpn("3 4 + 2 *"))
print(evaluate_rpn("5 1 2 + 4 * + 3 -"))