from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        schar_set = set(source)
        tchar_set = set(target)
        for c in tchar_set:
            if c not in schar_set:
                return - 1

        idx_nextindices = defaultdict(list)
        nextindices = [- 1 for _ in range(26)]
        for i in range(len(source) - 1, - 1, - 1):
            idx_nextindices[i] = nextindices[:]
            nextindices[ord(source[i]) - ord('a')] = i
        idx_nextindices[- 1] = nextindices[:]

        idx = - 1
        res = 1
        for c in target:
            idx = idx_nextindices[idx][ord(c) - ord('a')]
            if idx == - 1:
                idx = idx_nextindices[idx][ord(c) - ord('a')]
                res += 1
        return res
    
# time O(n + m)
# space O(n), due to hashmap
# using hashmap and snapshot of hashmap