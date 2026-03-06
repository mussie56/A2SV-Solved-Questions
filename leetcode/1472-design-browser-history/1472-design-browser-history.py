class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.last = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode

    def back(self, steps: int) -> str:
        while self.last != self.head and steps > 0:
            self.last = self.last.prev
            steps-=1
        return self.last.val

    def forward(self, steps: int) -> str:
        while self.last.next and steps > 0:
            self.last = self.last.next
            steps-=1
        return self.last.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)