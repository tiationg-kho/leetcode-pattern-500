from collections import defaultdict
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        heap = []
        for num, freq in num_freq.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        return [num for freq, num in heap]

# time O(n + nlogk)
# space O(n + k), due to hashmap and heap
# using heap and top k problem (based on heap) and min heap and hashmap

from collections import defaultdict
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        heap = [(- freq, num) for num, freq in num_freq.items()]
        heapify(heap)
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res

# time O(n + n + klogn)
# space O(n), due to hashmap and heap
# using heap and top k problem (based on heap) and max heap and hashmap

from collections import defaultdict
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        vals = [(f, n) for n, f in num_freq.items()]
        
        def quick_select(left, right):
            pivot_idx = random.randint(left, right)
            pivot_val = vals[pivot_idx]
            vals[right], vals[pivot_idx] = vals[pivot_idx], vals[right]
            partition_idx = left
            for i in range(left, right):
                if vals[i][0] < pivot_val[0]:
                    vals[i], vals[partition_idx] = vals[partition_idx], vals[i]
                    partition_idx += 1
            vals[right], vals[partition_idx] = vals[partition_idx], vals[right]
            return partition_idx

        left, right = 0, len(vals) - 1
        while left <= right:
            idx = quick_select(left, right)
            if idx == len(vals) - k:
                return [n for f, n in vals[idx:]]
            elif idx > len(vals) - k:
                right = idx - 1
            else:
                left = idx + 1
        
# time O(n**2) in worst, O(n) in average (notice that quick sort is O(nlogn) in average)
# space O(n), due to hashmap and list
# using array and sort and top k problem (based on sort) and quick select and hashmap

from collections import defaultdict
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        min_freq = min(num_freq.values())
        max_freq = max(num_freq.values())
        buckets = [[] for _ in range(max_freq - min_freq + 1)]
        for n, f in num_freq.items():
            buckets[f - min_freq].append(n)
        
        res = []
        for i in range(len(buckets) - 1, - 1, - 1):
            vals = buckets[i]
            if len(vals) <= k:
                res.extend(vals)
                k -= len(vals)
            else:
                break
        return res

# time O(n + b)
# space O(n + b)
# using array and sort and top k problem (based on sort) and bucket sort and hashmap