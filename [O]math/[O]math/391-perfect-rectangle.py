from collections import defaultdict
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        point_freq = defaultdict(int)
        area = 0
        for x, y, a, b in rectangles:
            point_freq[(x, y)] += 1
            point_freq[(a, b)] += 1
            point_freq[(a, y)] += 1
            point_freq[(x, b)] += 1
            area += (a - x) * (b - y)

        corners = []
        for p, f in point_freq.items():
            if f == 1:
                corners.append(p)
            elif f == 2:
                continue
            elif f == 4:
                continue
            else:
                return False
        if len(corners) != 4:
            return False
        
        x, y, a, b = float('inf'), float('inf'), float('-inf'), float('-inf')
        for p, q in corners:
            x = min(x, p)
            y = min(y, q)
            a = max(a, p)
            b = max(b, q)
        if (a - x) * (b - y) != area:
            return False
        return True
    
# time O(n)
# space O(n)
# using math and hashmap