class Node:
    def __init__(self,val="",next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.indicator = Node(homepage,None,None)

    def visit(self, url: str) -> None:
        new_hist = Node(url,None,self.indicator)
        self.indicator.next = new_hist
        self.indicator = self.indicator.next


    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.indicator and self.indicator.prev:
                self.indicator = self.indicator.prev
            else:
                break
        return self.indicator.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.indicator and self.indicator.next:
                self.indicator = self.indicator.next
            else:
                break
        return self.indicator.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)