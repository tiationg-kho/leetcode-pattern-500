class HitCounter:
    def __init__(self):
        self.limit = 300
        self.timestamp_count = [[0, 0] for _ in range(self.limit)]

    def hit(self, timestamp: int) -> None:
        idx = timestamp % self.limit
        if self.timestamp_count[idx][0] == timestamp:
            self.timestamp_count[idx][1] += 1
        else:
            self.timestamp_count[idx] = [timestamp, 1]

    def getHits(self, timestamp: int) -> int:
        res = 0
        idx = timestamp % self.limit
        for t, c in self.timestamp_count:
            if timestamp - self.limit < t <= timestamp:
                res += c
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# time O(1)
# space O(s), s is 300
# using array and circular array