class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            while 1 <= nums[i] <= len(nums):
                target_idx = nums[i] - 1
                if nums[i] == nums[target_idx]:
                    break
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        res = []
        for i, num in enumerate(nums):
            if i != num - 1:
                res.append(num)
        return res
        
# time O(n)
# space O(1), not counting output list
# using array and specific range array (cyclic sort)