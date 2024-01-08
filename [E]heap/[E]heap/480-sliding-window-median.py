from heapq import *
from collections import defaultdict
class TwoHeap:
    def __init__(self):
        self.smallhalf_maxheap = []
        self.largehalf_minheap = []
        self.removeval_freq = defaultdict(int)
        self.smallhalf_size = 0
        self.largehalf_size = 0

    def insert(self, val):
        if self.smallhalf_maxheap and - self.smallhalf_maxheap[0] >= val:
            heappush(self.smallhalf_maxheap, - val)
            self.smallhalf_size += 1
        else:
            heappush(self.largehalf_minheap, val)
            self.largehalf_size += 1
        
        self.balance()
        self.lazy_remove()
    
    def remove(self, val):
        if self.smallhalf_maxheap and - self.smallhalf_maxheap[0] == val:
            heappop(self.smallhalf_maxheap)
            self.smallhalf_size -= 1
        elif self.largehalf_minheap and self.largehalf_minheap[0] == val:
            heappop(self.largehalf_minheap)
            self.largehalf_size -= 1
        elif self.smallhalf_maxheap and - self.smallhalf_maxheap[0] > val:
            self.smallhalf_size -= 1
            self.removeval_freq[val] += 1
        else:
            self.largehalf_size -= 1
            self.removeval_freq[val] += 1
        
        self.balance()
        self.lazy_remove()

    def balance(self):
        if self.smallhalf_size > self.largehalf_size + 1:
            heappush(self.largehalf_minheap, - heappop(self.smallhalf_maxheap))
            self.smallhalf_size -= 1
            self.largehalf_size += 1
        if self.largehalf_size > self.smallhalf_size + 1:
            heappush(self.smallhalf_maxheap, - heappop(self.largehalf_minheap))
            self.largehalf_size -= 1
            self.smallhalf_size += 1

    def lazy_remove(self):
        while self.smallhalf_maxheap and self.removeval_freq[- self.smallhalf_maxheap[0]]:
            neg_val = heappop(self.smallhalf_maxheap)
            self.removeval_freq[- neg_val] -= 1
        while self.largehalf_minheap and self.removeval_freq[self.largehalf_minheap[0]]:
            val = heappop(self.largehalf_minheap)
            self.removeval_freq[val] -= 1

    def get_median(self):
        if self.smallhalf_size == self.largehalf_size:
            return (- self.smallhalf_maxheap[0] + self.largehalf_minheap[0]) / 2
        elif self.smallhalf_size > self.largehalf_size:
            return - self.smallhalf_maxheap[0]
        else:
            return self.largehalf_minheap[0]

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        twoheap = TwoHeap()
        res = []
        left = 0
        for right, num in enumerate(nums):
            twoheap.insert(nums[right])
            if right - left + 1 == k:
                res.append(twoheap.get_median())
                twoheap.remove(nums[left])
                left += 1
        return res
    
# time O(nlogn)
# space O(n)
# using heap and two heap problem and lazy removal and sliding window