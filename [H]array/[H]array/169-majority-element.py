class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        vote = 0
        for num in nums:
            if num == cand:
                vote += 1
            elif cand == None:
                cand = num
                vote = 1
            else:
                vote -= 1
                if vote == 0:
                    cand = None
        return cand

# time O(n)
# space O(1)
# using array and boyer moore vote algorithm