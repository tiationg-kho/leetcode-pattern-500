from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.num_indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_indices[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.num_indices[target]
        return random.choice(indices)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# time O(1) for pick()
# space O(n), due to hashmap
# using hashmap

import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        stream = 0
        res = None
        for i, num in enumerate(self.nums):
            if num == target:
                if 0 == random.randint(0, stream):
                    res = i
                stream += 1
        return res
        
# time O(n) for pick()
# space O(1)
# using array and reservoir sampling