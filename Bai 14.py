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

def stock_span(prices):
    stack = Stack()
    result = []
    
    for i in range(len(prices)):
        while not stack.isEmpty() and prices[stack.top()] <= prices[i]:
            stack.pop()
        
        if stack.isEmpty():
            span = i + 1
        else:
            span = i - stack.top()
        
        result.append(span)
        stack.push(i)
    
    return result

prices1 = [100, 80, 60, 70, 60, 75, 85]
prices2 = [10, 4, 5, 90, 120, 80]

print(stock_span(prices1))
print(stock_span(prices2))