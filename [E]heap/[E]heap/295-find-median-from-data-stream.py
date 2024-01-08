from heapq import *
class MedianFinder:

    def __init__(self):
        self.smallhalf_maxheap = []
        self.largehalf_minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.smallhalf_maxheap, - num)
        heappush(self.largehalf_minheap, - heappop(self.smallhalf_maxheap))
        if len(self.largehalf_minheap) > len(self.smallhalf_maxheap) + 1:
            heappush(self.smallhalf_maxheap, - heappop(self.largehalf_minheap))

    def findMedian(self) -> float:
        if len(self.largehalf_minheap) > len(self.smallhalf_maxheap):
            return self.largehalf_minheap[0]
        return (self.largehalf_minheap[0] + (- self.smallhalf_maxheap[0])) / 2

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
