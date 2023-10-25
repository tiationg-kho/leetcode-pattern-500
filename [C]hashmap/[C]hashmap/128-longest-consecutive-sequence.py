class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        res = 0
        for num in hashset:
            if num - 1 in hashset:
                continue
            if num + res not in hashset:
                continue
            cur = num
            while cur + 1 in hashset:
                cur = cur + 1
            res = max(res, cur - num + 1)
        return res
    
# time O(n)
# sapce O(n)
# using hashmap and store val and hashset and pruning
'''
1. find every sequence's start point
'''