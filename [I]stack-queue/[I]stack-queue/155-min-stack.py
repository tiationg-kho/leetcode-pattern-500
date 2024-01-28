class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:
        if self.min_num == None:
            self.stack.append(0)
            self.min_num = val
        elif val < self.min_num:
            self.stack.append(val - self.min_num)
            self.min_num = val
        else:
            self.stack.append(val - self.min_num)

    def pop(self) -> None:
        diff = self.stack.pop()
        if len(self.stack) == 0:
            self.min_num = None
        elif diff < 0:
            self.min_num += abs(diff)

    def top(self) -> int:
        diff = self.stack[- 1]
        if diff < 0:
            return self.min_num
        return self.min_num + diff

    def getMin(self) -> int:
        return self.min_num

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# time O(1)
# space O(n)
# using stack and queue and implement stack/queue and one stack