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

def next_greater_element(arr):
    stack = Stack()
    result = [-1] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        while not stack.isEmpty() and stack.top() <= arr[i]:
            stack.pop()
        if not stack.isEmpty():
            result[i] = stack.top()
        stack.push(arr[i])
    
    return result

print(next_greater_element([2, 1, 3]))
print(next_greater_element([4, 5, 2, 25]))
print(next_greater_element([13, 7, 6, 12]))