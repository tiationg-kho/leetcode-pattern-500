from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.val_freq = defaultdict(int)
        self.freq_stack = defaultdict(list)

    def push(self, val: int) -> None:
        self.val_freq[val] += 1
        freq = self.val_freq[val]
        if freq > self.max_freq:
            self.max_freq = freq
        self.freq_stack[freq].append(val)

    def pop(self) -> int:
        vals = self.freq_stack[self.max_freq]
        val = vals.pop()
        if len(vals) == 0:
            self.freq_stack.pop(self.max_freq)
            self.max_freq -= 1
        self.val_freq[val] -= 1
        if self.val_freq[val] == 0:
            self.val_freq.pop(val)
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# time O(1)
# space O(n)
# using stack and queue and implement stack/queue and stack and hashmap