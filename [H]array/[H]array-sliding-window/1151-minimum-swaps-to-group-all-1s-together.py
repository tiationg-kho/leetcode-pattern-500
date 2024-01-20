class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count_total = 0
        for num in data:
            if num == 1:
                count_total += 1
        
        res = count_total
        count = 0
        left = 0
        for right in range(len(data)):
            if data[right] == 1:
                count += 1
            while right - left + 1 > count_total:
                if data[left] == 1:
                    count -= 1
                left += 1
            if right - left + 1 == count_total:
                res = min(res, right - left + 1 - count)
        return res

# time O(n)
# space O(1)
# using array and standard sliding window