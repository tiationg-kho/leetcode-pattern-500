class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        def valid(diff):
            pairs = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > diff:
                    left += 1
                left_choices = right - left
                right_choices = 1
                pairs += left_choices * right_choices
            return pairs >= k

        left, right, boundary = 0, max(nums) - min(nums), - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(nlogn + nlogD), D is the max distance in nums
# space O(1)
# using binary search and search in sth’s range and sort and sliding window