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

def simulate_stack_operations(operations):
    stack = Stack()
    for op in operations:
        if op.startswith("push"):
            parts = op.split()
            value = int(parts[1])
            stack.push(value)
        elif op == "pop":
            result = stack.pop()
            if result is not None:
                print(result)
    print(stack.stack)

ops = ["push 5", "push 7", "pop", "push 3", "pop"]
simulate_stack_operations(ops)