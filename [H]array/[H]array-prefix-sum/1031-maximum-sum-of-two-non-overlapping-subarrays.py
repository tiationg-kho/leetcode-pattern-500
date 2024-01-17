class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total

        def get_sum(p, q):
            max_p = prefix[p]
            max_pq = prefix[p + q]
            for i in range(p + q, len(nums)):
                cur_p = prefix[i - q + 1] - prefix[i - p - q + 1]
                cur_q = prefix[i + 1] - prefix[i - q + 1]
                max_p = max(max_p, cur_p)
                max_pq = max(max_pq, cur_q + max_p)
            return max_pq

        return max(get_sum(firstLen, secondLen), get_sum(secondLen, firstLen))

# time O(n)
# space O(n)
# using array and prefix sum and standard prefix sum and sliding window
'''
1. subarrayA is before subarrayB
2. subarrayB is before subarrayA
3. prefix sum is just for simplify calc, can solve by sliding window only
'''