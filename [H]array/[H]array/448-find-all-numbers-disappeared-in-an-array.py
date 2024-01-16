class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            while 1 <= nums[i] <= len(nums):
                target_idx = nums[i] - 1
                if nums[i] == nums[target_idx]:
                    break
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        res = []
        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(i + 1)
        return res
    
# time O(n)
# space O(1), if not count output list
# using array and specific range array (cyclic sort)