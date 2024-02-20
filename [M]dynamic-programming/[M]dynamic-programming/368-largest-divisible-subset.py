class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        source = [- 1 for _ in range(len(nums))]
        length = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i - 1, - 1, - 1):
                if nums[i] % nums[j] == 0 and length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    source[i] = j
        
        max_length = max(length)
        res = []
        for i, l in enumerate(length):
            if l == max_length:
                while len(res) < max_length:
                    res.append(nums[i])
                    i = source[i]
                break

        return res[:: - 1]
    
# time O(n**2), due to each num has run a loop to check the nums before it
# space O(n)
# using dynamic programming and linear sequence and sort