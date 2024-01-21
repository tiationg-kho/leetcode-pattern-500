class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            target = - nums[i]
            while left < right:
                cur = nums[left] + nums[right]
                if cur == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                elif cur > target:
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return res
    
# time O(n**2)
# space O(1), or due to built in sort's cost
# using array and two pointers opposite direction and shrink type and sort
'''
1. be aware of handling duplicate
'''