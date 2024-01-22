class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]
        
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
                elif right == n- m:
                    res.append(left_part[left])
                    left += 1
                elif left_part[left] + right_part[right] >= right_part[right] + left_part[left]:
                    res.append(left_part[left])
                    left += 1
                else:
                    res.append(right_part[right])
                    right += 1
            return res

        nums = merge_sort(nums)
        res = ''.join(nums)
        return res if res[0] != '0' else '0'

# time O(nlogn), logn recursion layers and each layer costs O(n)
# space O(n), due to new list, recursion stack is O(logn)
# using array and sort and self defined merge sort
# stable

import random
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]
        
        def quick_sort(left, right):
            if left >= right:
                return
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            partition_idx = left
            for i in range(left, right):
                if nums[i] + pivot_val > pivot_val + nums[i]:
                    nums[i], nums[partition_idx] = nums[partition_idx], nums[i]
                    partition_idx += 1
            nums[right], nums[partition_idx] = nums[partition_idx], nums[right]
            quick_sort(left, partition_idx - 1)
            quick_sort(partition_idx + 1, right)
            return

        quick_sort(0, len(nums) - 1)
        res = ''.join(nums)
        return res if res[0] != '0' else '0'

# time O(n**2), when the list is almost sorted, and the average time is O(nlogn)
# space O(n), due to recursion layers, O(logn) in average
# using array and sort and self defined quick sort
# unstable