from heapq import *
class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_heap = []
        self.remove_set = set()
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.id))
        heappush(self.max_heap, (- x, - self.id))
        self.id += 1

    def pop(self) -> int:
        val, idx = self.stack.pop()
        self.remove_set.add(idx)
        self.lazy_remove()
        return val

    def top(self) -> int:
        return self.stack[- 1][0]

    def peekMax(self) -> int:
        return - self.max_heap[0][0]

    def popMax(self) -> int:
        neg_val, neg_idx = heappop(self.max_heap)
        self.remove_set.add(- neg_idx)
        self.lazy_remove()
        return - neg_val
    
    def lazy_remove(self):
        while self.stack and self.stack[- 1][1] in self.remove_set:
            _, idx = self.stack.pop()
            self.remove_set.remove(idx)
        while self.max_heap and - self.max_heap[0][1] in self.remove_set:
            _, neg_idx = heappop(self.max_heap)
            self.remove_set.remove(- neg_idx)

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# time O(logn) for push(), amortized O(logn) for pop(), popmax(), O(1) for init, top(), peekMax()
# space O(n)
# using stack and queue and implement stack/queue and stack and heap and hashmap