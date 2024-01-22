import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quick_select(left, right):
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            partition_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[i], nums[partition_idx] = nums[partition_idx], nums[i]
                    partition_idx += 1
            nums[partition_idx], nums[right] = nums[right], nums[partition_idx]
            return partition_idx

        left, right = 0, len(nums) - 1
        middle_idx = (left + right) // 2
        while left <= right:
            idx = quick_select(left, right)
            if idx == middle_idx:
                break
            elif idx > middle_idx:
                right = idx - 1
            else:
                left = idx + 1
        median = nums[middle_idx]

        left, right = 0, len(nums) - 1
        cur = 0
        while cur <= right:
            if nums[cur] < median:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == median:
                cur += 1
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
        
        clone_nums = nums[:]
        left, right = middle_idx, len(clone_nums) - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = clone_nums[left]
                left -= 1
            else:
                nums[i] = clone_nums[right]
                right -= 1

# time O(n), due to quick select (average), worst is O(n**2)
# space O(n)
# using array and sort and quick select and three way partitioning
'''
1. quick select to get median
2. three way partitioning
3. notice: how to avoid vals equal median place in neighbor
'''

import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quick_select(left, right):
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            partition_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[i], nums[partition_idx] = nums[partition_idx], nums[i]
                    partition_idx += 1
            nums[right], nums[partition_idx] = nums[partition_idx], nums[right]
            return partition_idx

        left, right = 0, len(nums) - 1
        mid_val = None
        while left <= right:
            idx = quick_select(left, right)
            if idx == len(nums) // 2:
                mid_val = nums[idx]
                break
            elif idx > len(nums) // 2:
                right = idx - 1
            else:
                left = idx + 1
        
        n = len(nums)
        small = n - 1 if (n - 1) % 2 == 0 else n - 2 # largest even idx (even idx for small val)
        i = small # for traversing whole array
        large = 1 # smallest odd idx (odd idx for large val)
        for _ in range(n):
            if nums[i] < mid_val:
                nums[small], nums[i] = nums[i], nums[small]
                small -= 2
                i -= 2
                if i < 0:
                    i = n - 1 if (n - 1) % 2 == 1 else n - 2 # reset to the largest odd idx
            elif nums[i] > mid_val:
                nums[large], nums[i] = nums[i], nums[large]
                large += 2
            else:
                i -= 2
                if i < 0:
                    j = n - 1 if (n - 1) % 2 == 1 else n - 2 # reset to the largest odd idx

# time O(n), due to quick select (average), worst is O(n**2)
# space O(1)
# using array and sort and quick select and three way partitioning
'''
1. quick select to get median
2. three way partitioning
3. notice: how to avoid vals equal median place in neighbor
'''