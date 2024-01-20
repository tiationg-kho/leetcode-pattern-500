from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type_freq = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(fruits)):
            type_freq[fruits[right]] += 1
            while len(type_freq) > 2:
                type_freq[fruits[left]] -= 1
                if type_freq[fruits[left]] == 0:
                    type_freq.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)
        return res
    
# time O(n)
# space O(1)
# using array and standard sliding window and hashmap