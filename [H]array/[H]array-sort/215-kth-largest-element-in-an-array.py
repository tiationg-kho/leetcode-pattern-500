import random
from collections import defaultdict
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        key_with_max_freq = max(num_freq, key=num_freq.get)
        max_freq = max(num_freq.values())
        if max_freq > k and max_freq > len(nums) - k:
            return key_with_max_freq
        
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
                return nums[idx]
            elif idx > len(nums) - k:
                right = idx - 1
            else:
                left = idx + 1
        
# time O(n**2) in worst, O(n) in average (notice that quick sort is O(nlogn) in average)
# space O(n), due to hashmap
# using array and sort and top k problem (based on sort) and quick select and prune

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        num_freq = [0 for _ in range(max_num - min_num + 1)]
        for num in nums:
            num_freq[num - min_num] += 1
        for i in range(len(num_freq) - 1, - 1, - 1):
            if num_freq[i] >= k:
                return i + min_num
            k -= num_freq[i]

# time O(n+b)
# space O(b), b is the range of min_num and max_num
# using array and sort and top k problem (based on sort) and bucket sort