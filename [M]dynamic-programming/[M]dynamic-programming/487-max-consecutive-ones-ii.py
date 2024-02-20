class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        flip = 0
        non_flip = 0
        for num in nums:
            if num == 1:
                flip += 1
                non_flip += 1
            else:
                flip = non_flip + 1
                non_flip = 0
            res = max(res, flip, non_flip)
        return res
    
# time O(n)
# space O(1)
# using dynamic programming and linear sequence

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0
        flip = 0
        for right in range(len(nums)):
            if nums[right] != 1:
                flip += 1
            while flip > 1:
                if nums[left] == 0:
                    flip -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# time O(n)
# space O(1)
# using array and standard sliding window