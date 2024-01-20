class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        while p1 < len(version1) or p2 < len(version2):
            v1, v2 = 0, 0
            while p1 < len(version1) and version1[p1] != '.':
                v1 *= 10
                v1 += int(version1[p1])
                p1 += 1
            while p2 < len(version2) and version2[p2] != '.':
                v2 *= 10
                v2 += int(version2[p2])
                p2 += 1
            if v1 < v2:
                return - 1
            elif v1 > v2:
                return 1
            if p1 < len(version1) and version1[p1] == '.':
                p1 += 1
            if p2 < len(version2) and version2[p2] == '.':
                p2 += 1
        return 0

# time O(n+m)
# space O(1)
# using array and two pointers same direction and traverse two sequences