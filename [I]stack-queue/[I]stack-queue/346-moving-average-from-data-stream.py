from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.queue = deque([])

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# time O(1)
# space O(n)
# using stacka and queue and use queue to simulate