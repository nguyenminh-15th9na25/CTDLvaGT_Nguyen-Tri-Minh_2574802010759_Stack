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

def largest_rectangle_area(heights):
    stack = Stack()
    max_area = 0
    i = 0
    
    while i < len(heights):
        if stack.isEmpty() or heights[i] >= heights[stack.top()]:
            stack.push(i)
            i += 1
        else:
            top = stack.pop()
            if stack.isEmpty():
                area = heights[top] * i
            else:
                area = heights[top] * (i - stack.top() - 1)
            max_area = max(max_area, area)
    
    while not stack.isEmpty():
        top = stack.pop()
        if stack.isEmpty():
            area = heights[top] * i
        else:
            area = heights[top] * (i - stack.top() - 1)
        max_area = max(max_area, area)
    
    return max_area

print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
print(largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]))