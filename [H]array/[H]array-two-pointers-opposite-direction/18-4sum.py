class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j - 1 >= i + 1 and nums[j - 1] == nums[j]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
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
    
# time O(n**3)
# space O(1), not count output list
# using array and two pointers opposite direction and shrink type and sort