class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, boundary = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] < nums[boundary]:
                boundary = m
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m - 1
        return nums[boundary]

# time O(logn)
# space O(1)
# using binary search and rotated sorted array
'''
notice above soltion depends on all elements are unique
if elements are not unique, then:

left, right, boundary = 0, len(nums) - 1, len(nums) - 1
while left <= right:
    m = (left + right) // 2
    if nums[m] < nums[boundary]:
        boundary = m
    if nums[m] > nums[right]:
        left = m + 1
    elif nums[m] < nums[right]:
        right = m - 1
    else:
        right -= 1
return nums[boundary]

# time O(n)
# space O(1)
# using binary search and rotated sorted array
'''