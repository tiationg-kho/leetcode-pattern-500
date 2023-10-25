class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, num in enumerate(nums):
            if target - num in num_idx:
                return [i, num_idx[target - num]]
            num_idx[num] = i
        return []
        
# time O(n), due to traverse
# space O(n), due to hashmap
# using hashmap and store val