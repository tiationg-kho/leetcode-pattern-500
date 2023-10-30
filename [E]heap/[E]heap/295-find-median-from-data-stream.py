from heapq import *
class MedianFinder:

    def __init__(self):
        self.maxheap_smallhalf = []
        self.minheap_largehalf = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap_smallhalf, - num)
        heappush(self.minheap_largehalf, heappop(self.maxheap_smallhalf) * (- 1))

        if len(self.minheap_largehalf) - len(self.maxheap_smallhalf) > 1:
            heappush(self.maxheap_smallhalf, heappop(self.minheap_largehalf) * (- 1))

    def findMedian(self) -> float:
        if (len(self.minheap_largehalf) + len(self.maxheap_smallhalf)) % 2 == 0:
            return (self.maxheap_smallhalf[0] * (- 1) + self.minheap_largehalf[0]) / 2
        return self.minheap_largehalf[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# time O(logn) for addNum(), O(1) for findMedian()
# space O(n), due to heap
# using heap and two heap problem
'''
follow up
bucket sort's idea
if input are in some small range, just build an array to record each number's count, then iterate over array to get median
also if most input are in some small range, will need build two counters to record number beyond range
'''
