class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total

        res = float('inf')
        res_idx = - 1
        for i in range(len(nums)):
            first_avg = prefix[i + 1] // (i + 1)
            second_avg = (prefix[- 1] - prefix[i + 1]) // (len(nums) - i - 1) if len(nums) - i - 1 != 0 else 0
            diff = abs(first_avg - second_avg)
            if diff < res:
                res = diff
                res_idx = i
        return res_idx
    
# time O(n)
# space O(n)
# using array and prefix sum and standard prefix sum