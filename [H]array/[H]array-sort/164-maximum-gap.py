class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        if min_num == max_num or len(nums) < 2:
            return 0

        interval = max(1, (max_num - min_num) // len(nums))
        buckets_count = (max_num - min_num) // interval + 1
        buckets = [[False, float('inf'), float('-inf')] for _ in range(buckets_count)]
        for num in nums:
            idx = (num - min_num) // interval
            buckets[idx] = [True, min(buckets[idx][1], num), max(buckets[idx][2], num)]
        
        buckets = [[min_val, max_val] for filled, min_val, max_val in buckets if filled]
        res = 0
        for i in range(1, len(buckets)):
            res = max(res, buckets[i][0] - buckets[i - 1][1])

        return res
    
# time O(n + b)
# space O(b)
# using array and sort and bucket sort and pigeonhole principle
'''
1. pigeonhole principle
2. n+1 pigeons live in n holes, at least one hole have two or more pigeons
3. n pigeons live in n+1 holes, at least one hole is empty
4. so we need to make buckets more than length of nums
5. if there is a empty hole, 
   the maximum difference cannot be within a single bucket but between the numbers in different buckets
6. even if all buckets are filled, 
   the maximum gap is still likely to occur between the maximum value of one bucket and the minimum value of an adjacent bucket
   this is because the numbers within each bucket are relatively close to each other, given the way the interval size is determined
'''