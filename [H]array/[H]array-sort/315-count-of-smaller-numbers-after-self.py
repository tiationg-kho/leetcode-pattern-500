class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        counts = [0 for _ in range(len(nums))]
        nums = [(num, i) for i, num in enumerate(nums)]
        
        def merge_sort(nums):
            n = len(nums)
            if n <= 1:
                return nums
            m = n // 2
            left_part = merge_sort(nums[: m])
            right_part = merge_sort(nums[m:])
            res = []
            left, right = 0, 0
            while left < m or right < n - m:
                if left == m:
                    res.append(right_part[right])
                    right += 1
                elif right == n - m:
                    res.append(left_part[left])
                    counts[left_part[left][1]] += right
                    left += 1
                elif left_part[left][0] <= right_part[right][0]:
                    res.append(left_part[left])
                    counts[left_part[left][1]] += right
                    left += 1
                else:
                    res.append(right_part[right])
                    right += 1
            return res

        merge_sort(nums)
        return counts

# time O(nlogn), each layer to merge cost O(n)
# space O(n), due to new list, merge sort has logn stack layers
# using array and sort and merge sort
'''
1. the count is updated for each element from the left part during merging
   (think about how many elements from right part and place before cur element)
   (means these elements are smaller than cur element and locate at cur elements right side before sorting)
'''