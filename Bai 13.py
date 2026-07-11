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

def dfs_iterative(graph, start):
    stack = Stack()
    visited = set()
    stack.push(start)
    result = []
    
    while not stack.isEmpty():
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.push(neighbor)
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph2 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print(dfs_iterative(graph, 'A'))
print(dfs_iterative(graph2, 2))