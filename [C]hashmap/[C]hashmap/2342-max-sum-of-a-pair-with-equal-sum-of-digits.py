class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        total_num = {}
        res = - 1
        for num in nums:
            total, val = 0, num
            while val:
                d, m = divmod(val, 10)
                total += m
                val = d
            if total not in total_num:
                total_num[total] = num
            else:
                res = max(res, total_num[total] + num)
                total_num[total] = max(total_num[total], num)
        return res
    
# time O(nL), can treat L as constant
# space O(n)
# using hashmap and store val