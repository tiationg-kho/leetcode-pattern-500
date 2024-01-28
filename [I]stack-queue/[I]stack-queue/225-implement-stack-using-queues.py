from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        old_element_count = len(self.queue)
        self.queue.append(x)
        for _ in range(old_element_count):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# time O(n), due to push, and others are O(1)
# space O(n), due to queue
# using stack and queue and implement stack/queue and one queue