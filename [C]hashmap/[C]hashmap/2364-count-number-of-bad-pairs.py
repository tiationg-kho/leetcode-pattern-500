from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        val_freq = defaultdict(int)
        for i, num in enumerate(nums):
            good_pairs += val_freq[num - i]
            val_freq[num - i] += 1
        total_pairs = (len(nums) * (len(nums) - 1)) // (2 * 1)
        return total_pairs - good_pairs

# time O(n)
# space O(n)
# using hashmap
'''
1. j - i == nums[j] - nums[i] => nums[j] - j == nums[i] - i
'''