class Solution:
    def canChange(self, start: str, target: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(start) or p2 < len(target):
            c1 = None
            while p1 < len(start):
                if start[p1] == 'L' or start[p1] == 'R':
                    c1 = start[p1]
                    break
                p1 += 1
            c2 = None
            while p2 < len(target):
                if target[p2] == 'L' or target[p2] == 'R':
                    c2 = target[p2]
                    break
                p2 += 1
            if c1 != c2:
                return False
            elif c1 == 'L' and p1 < p2:
                return False
            elif c1 == 'R' and p1 > p2:
                return False
            p1 += 1
            p2 += 1
        return True
    
# time O(n)
# space O(1)
# using array and two pointers same direction and traverse two sequences