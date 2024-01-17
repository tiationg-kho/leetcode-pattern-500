class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            if e1 < s2:
                i += 1
            elif e2 < s1:
                j += 1
            else:
                res.append([max(s1, s2), min(e1, e2)])
                if e1 > e2:
                    j += 1
                else:
                    i += 1

        return res
    
# time O(m+n)
# space O(m+n), for output list
# using array and line sweep and compare two intervals each round and two pointers and greedy