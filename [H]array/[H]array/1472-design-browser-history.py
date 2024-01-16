class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.start = 0
        self.cur = 0
        self.end = 0
        
    def visit(self, url: str) -> None:
        if self.cur + 1 == len(self.pages):
            self.pages.append(url)
            self.cur += 1
            self.end = self.cur
        else:
            self.pages[self.cur + 1] = url
            self.cur += 1
            self.end = self.cur

    def back(self, steps: int) -> str:
        if self.cur - steps >= self.start:
            self.cur -= steps
            return self.pages[self.cur]
        else:
            self.cur = self.start
            return self.pages[self.cur]

    def forward(self, steps: int) -> str:
        if self.cur + steps <= self.end:
            self.cur += steps
            return self.pages[self.cur]
        else:
            self.cur = self.end
            return self.pages[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# time O(1) for all
# space O(n)
# using array and maintain array's range dynamically