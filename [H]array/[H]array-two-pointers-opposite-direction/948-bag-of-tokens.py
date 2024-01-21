class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()

        res = 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                res = max(res, score)
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return res
        
# time O(nlogn)
# space O(1), or due to built in sort
# using array and two pointers opposite direction and shrink type and sort and greedy