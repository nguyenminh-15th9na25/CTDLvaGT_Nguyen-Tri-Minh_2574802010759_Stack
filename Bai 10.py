from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, value):
        self.q1.append(value)
    
    def pop(self):
        if not self.q1:
            print("Stack is empty!")
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result
    
    def top(self):
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return result
    
    def isEmpty(self):
        return len(self.q1) == 0

sq = StackUsingQueues()
sq.push(1)
sq.push(2)
sq.push(3)
print(sq.pop())
print(sq.pop())
print(sq.pop())