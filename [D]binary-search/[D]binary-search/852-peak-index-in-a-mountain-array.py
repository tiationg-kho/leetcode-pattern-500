class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right, boundary = 1, len(arr) - 2, - 1
        while left <= right:
            m = (left + right) // 2
            if arr[m - 1] < arr[m]:
                boundary = m
                left = m + 1
            else:
                right = m - 1
        return boundary

# time O(logn), due to binary search
# space O(1)
# using binary search and use boundary to record