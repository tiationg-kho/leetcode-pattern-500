from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.x_points = defaultdict(set)
        self.point_freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.x_points[point[0]].add((point[0], point[1]))
        self.point_freq[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        points = self.x_points[point[0]]
        for x, y in points:
            if y == point[1]:
                continue
            edge = abs(y - point[1])
            res += self.point_freq[(x - edge, y)] * self.point_freq[(x - edge, point[1])] * self.point_freq[(x, y)]
            res += self.point_freq[(x + edge, y)] * self.point_freq[(x + edge, point[1])] * self.point_freq[(x, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# time O(1) for init and add(), O(n) for count
# space O(n)
# using hashmap and store valid val’s freq for finding pairs