class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total

        for i in range(len(nums)):
            if prefix[i] == prefix[len(nums)] - prefix[i + 1]:
                return i
        return - 1
    
# time O(n)
# space O(n)
# using array and prefix sum and standard prefix sum