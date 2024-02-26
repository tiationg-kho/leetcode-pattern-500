class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify = False
        for i, num in enumerate(nums):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                if modify:
                    return False
                modify = True
                large, small = nums[i], nums[i + 1]
                if i - 1 < 0 or nums[i - 1] <= small:
                    nums[i] = small
                else:
                    nums[i + 1] = large
        return True

# time O(n)
# space O(1)
# using greedy
'''
1. [5, 8, 3, 9], [1, 3, 2, 2]
2. sometimes change to larger one, sometimes change to smaller one
'''