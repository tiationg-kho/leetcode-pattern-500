class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_total = 0
        for num in nums:
            if num == 1:
                count_total += 1
        
        res = count_total
        count = 0
        left = 0
        for right in range(len(nums) * 2):
            mod_right = right % len(nums)
            if nums[mod_right] == 1:
                count += 1
            while right - left + 1 > count_total:
                mod_left = left % len(nums)
                if nums[mod_left] == 1:
                    count -= 1
                left += 1
            if right - left + 1 == count_total:
                res = min(res, right - left + 1 - count)
        return res

# time O(n)
# space O(1)
# using array and standard sliding window