import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin_nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.origin_nums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 1, - 1, - 1):
            target_idx = random.randint(0, i)
            self.nums[i], self.nums[target_idx] = self.nums[target_idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# time O(n)
# space O(n)
# using array and knuth shuffle