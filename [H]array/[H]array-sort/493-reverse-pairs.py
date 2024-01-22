class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        count = 0
        
        def merge_sort(nums):
            nonlocal count
            n = len(nums)
            if n <= 1:
                return nums
            m = n // 2
            left_part = merge_sort(nums[: m])
            right_part = merge_sort(nums[m:])

            left, right = 0, 0
            while left < m and right < n - m:
                if left_part[left] > right_part[right] * 2:
                    count += m - left
                    right += 1
                else:
                    left += 1

            res = []
            left, right = 0, 0
            while left < m or right < n - m:
                if left == m:
                    res.append(right_part[right])
                    right += 1
                elif right == n - m:
                    res.append(left_part[left])
                    left += 1
                elif left_part[left] <= right_part[right]:
                    res.append(left_part[left])
                    left += 1
                else:
                    res.append(right_part[right])
                    right += 1
            return res

        merge_sort(nums)
        return count
            
# time O(nlogn), each layer to merge cost O(n)
# space O(n), due to new list, merge sort has logn stack layers
# using array and sort and merge sort and two pointers
'''
1. the count is updated if left part element is twice larger than right part element
'''