class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total

        for j in range(3, len(nums) - 3):
            prefix_set = set()
            for i in range(1, j - 1):
                if prefix[i] == prefix[j] - prefix[i + 1]:
                    prefix_set.add(prefix[i])
            for k in range(j + 2, len(nums) - 1):
                if prefix[k] - prefix[j + 1] == prefix[- 1] - prefix[k + 1]:
                    if prefix[k] - prefix[j + 1] in prefix_set:
                        return True
        return False
        
# time O(n**2)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray       
'''
1. xixjxkx
   0123456
'''