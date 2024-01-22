class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        max_box_size = max(boxTypes, key = lambda x: x[1])[1]
        min_box_size = min(boxTypes,  key = lambda x: x[1])[1]

        buckets = [0 for _ in range(max_box_size - min_box_size + 1)]
        for count, size in boxTypes:
            buckets[size - min_box_size] += count
        
        res = 0
        for i in range(len(buckets) - 1, - 1, - 1):
            if buckets[i] <= truckSize:
                res += buckets[i] * (i + min_box_size)
                truckSize -= buckets[i]
            elif truckSize:
                res += truckSize * (i + min_box_size)
                truckSize -= truckSize
            else:
                break
        return res

# time O(n+b)
# space O(b)
# using array and sort and bucket sort and greedy