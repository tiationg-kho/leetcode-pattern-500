from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        tail_freq = defaultdict(int)
        for num in nums:
            if num_freq[num] == 0:
                continue
            num_freq[num] -= 1
            if tail_freq[num - 1] > 0:
                tail_freq[num - 1] -= 1
                tail_freq[num] += 1
            elif num_freq[num + 1] and num_freq[num + 2]:
                num_freq[num + 1] -= 1
                num_freq[num + 2] -= 1
                tail_freq[num + 2] += 1
            else:
                return False
        return True
        
# time O(n)
# space O(n)
# using greedy and hashmap