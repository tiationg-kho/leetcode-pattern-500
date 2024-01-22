class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        buckets = [0 for _ in range(max_num - min_num + 1)]
        for num in nums:
            buckets[num - min_num] += 1

        res = - 1
        left, right = 0, len(buckets) - 1
        while left <= right:
            cur = left + min_num + right + min_num
            if buckets[left] == 0:
                left += 1
            elif buckets[right] == 0:
                right -= 1
            elif left == right and buckets[left] < 2:
                break
            elif cur < k:
                res = max(res, cur)
                left += 1
            else:
                right -= 1
        return res

# time O(n + b)
# space O(b)
# using array and sort and bucket sort and two pointers