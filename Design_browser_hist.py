class Node:
    def __init__(self,value,prev=None,next=None):
        self.next = next
        self.prev = prev
        self.value = value

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        

    def visit(self, url: str) -> None:
        self.current.next = Node(url, self.current)
        self.current = self.current.next
                
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev == None:
                break
            self.current = self.current.prev

        return self.current.value

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next == None:
                break
            self.current = self.current.next
        return self.current.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
