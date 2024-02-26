class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        first_neg = None

        res = 0
        for i, num in enumerate(nums):
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
                if first_neg == None:
                    first_neg = i
            else:
                pos = 0
                neg = 0
                first_neg = None

            if neg == 0:
                res = max(res, pos)
            elif neg % 2 == 0:
                res = max(res, pos + neg)
            else:
                res = max(res, i - first_neg)
        
        return res
    
# time O(n)
# space O(1)
# using greedy