class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        i, j = - 1, - 1
        for k, word in enumerate(wordsDict):
            if word == word1:
                i = k
            if word == word2:
                j = k
            if i != - 1 and j != - 1:
                res = min(res, abs(i - j))
            if res == 1:
                break
        return res
    
# time O(nL)
# space O(1)
# using array and traverse