class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        last_small = 1
        last_large = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                last_large = last_small + 1
            elif nums[i - 1] > nums[i]:
                last_small = last_large + 1
        return max(last_small, last_large)

# time O(n)
# space O(1)
# using dynamic programming and linear sequence
'''
1. if nums[i - 1] < nums[i], we can use seq with last_small and cur element to form new subseq
2. the last small subseq might use nums[i - 1] as last element, then add nums[i] to subseq is valid
3. the last small subseq might not use nums[i - 1] as last element, means its last element is smaller then nums[i - 1], then add nums[i] to subseq is also valid
'''