class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            a = self.stack.popleft() # [1, 2, 3] -> [2, 3, 1] -> [3, 2, 1] -> return self.stack.pop(0)
            self.stack.append(a)
        return self.stack.popleft()
    
    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True
