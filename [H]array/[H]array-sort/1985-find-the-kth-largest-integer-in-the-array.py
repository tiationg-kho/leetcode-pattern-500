from collections import defaultdict
import random
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        nums = [int(num) for num in nums]

        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        num_with_max_freq = max(num_freq, key=num_freq.get)
        max_freq = max(num_freq.values())
        if max_freq > k and max_freq > len(nums) - k:
            return str(num_with_max_freq)
        
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
            if idx == len(nums) - k:
                return str(nums[idx])
            elif idx > len(nums) - k:
                right = idx - 1
            else:
                left = idx + 1

# time O(n**2), quick select can be O(n) in average (O(n**2) in worst) (notice that quick sort is O(nlogn) in average)
# space O(n)
# using array and sort and top k problem (based on sort) and quick select and prune