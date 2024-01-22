import random
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
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
        while left <= right:
            idx = quick_select(left, right)
            if idx == len(nums) // 2:
                mid_val = nums[idx]
                res = 0
                for num in nums:
                    res += abs(num - mid_val)
                return res
            elif idx > len(nums) // 2:
                right = idx - 1
            else:
                left = idx + 1
    
# time O(n), due to quick select (average), worst is O(n**2)
# space O(1)
# using array and sort and quick select and math
'''
1. find median
2. if length is odd, then just use median
3. if length is even, choose any one of the two numbers in the median calculation
'''