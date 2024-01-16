class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        def get_top_k_majority(k):
            cand_vote = {}
            for num in nums:
                if num in cand_vote:
                    cand_vote[num] += 1
                elif len(cand_vote) < k:
                    cand_vote[num] = 1
                else:
                    for c in list(cand_vote.keys()):
                        cand_vote[c] -= 1
                        if cand_vote[c] == 0:
                            cand_vote.pop(c)

            for c in cand_vote.keys():
                cand_vote[c] = 0
            for num in nums:
                if num in cand_vote:
                    cand_vote[num] += 1
            return [c for c, v in cand_vote.items() if v * (k + 1) > len(nums)]

        return get_top_k_majority(2)
    
# time O(nk), k is 2 here
# space O(k)
# using array and boyer moore vote algorithm