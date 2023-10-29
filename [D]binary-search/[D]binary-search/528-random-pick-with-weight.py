import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0 for _ in range(len(w) + 1)]
        total = 0
        for i, weight in enumerate(w):
            total += weight
            self.prefix[i + 1] = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[- 1])
        left, right, boundary = 1, len(self.prefix) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if self.prefix[m] >= target:
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# time O(logn), for pickIndex() using binary search and initiation is O(n) due to prefix sum list
# space O(n), due to prefix sum list
# using binary search and search in a sorted array for most close val and prefix sum and random

'''
nums = [2, 8, 5]
prefix = [0, 2, 10, 15]
[1 2] [3 4 5 6 7 8 9 10] [11 12 13 14 15]
'''