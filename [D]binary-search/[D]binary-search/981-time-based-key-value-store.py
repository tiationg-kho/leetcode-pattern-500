from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        vals = self.store[key]
        left, right, boundary = 0, len(vals) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if vals[m][1] <= timestamp:
                boundary = m
                left = m + 1
            else:
                right = m - 1
        return vals[boundary][0] if boundary != - 1 else ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# time O(logn) for get()
# space O(n), due to hashmap, n is the number of calling set()
# using binary search and search in a sorted array for most close val and hashmap