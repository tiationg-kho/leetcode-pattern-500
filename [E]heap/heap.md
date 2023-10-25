# heap

## intro

- heap is a data structure (binary heap)
    - support insert in `O(log(n))`
        - insert as last element
        - swim up the last element
    - support delete_min or delete_max in `O(log(n))`
        - swap the top element with last element
        - pop last element (which is old top element)
        - sink down the (new) top element
    - heapify(nums) takes `O(n)` time
        - checking and performing sink down start from last element to top element
            - why sink down every element is not `O(nlogn)` time
                - because the higher layer, which node would cost more, actually have few nodes inside the layer
    - `O(1)` to get the min val in min heap, or max val in max heap
        - get the top element
- min heap
    - look like a complete binary tree
        - can be implement by array (using the complete tree’s attribute)
            - ignore first idx 0, start from idx 1
            - if node’s idx == i
                - parent node idx == i // 2
                - left child idx == 2 * i
                - right child idx == 2 * i + 1
    - for any node, its key is less than or equal to its children’s key
    - there is no comparable relationship between children
    - the height of a heap is guaranteed to be `O(log(n))`
    - in python, max heap can be simulated by min heap with negative value
    - we can use tuple to push multiple information inside the heap in one element if we need
    - in python, if the element inside the heap needs complex comparison, we can use self defined class and implement the less than method
        - eg. sort the words in ascending order of frequency. If words have the same frequency, sort them alphabetically in reverse order
    
    ```python
    class FreqWord:
        def __init__(self, f, w):
            self.f = f
            self.w = w
        
        def __lt__(self, other):
            if self.f == other.f:
                return self.w > other.w
            return self.f < other.f
    ```
    
    - we can use two heap to find median
        - maxheap_smallhalf
        - minheap_largehalf

## pattern

**greedily schedule tasks (start/end/val)**

- sort every task by their start time
- use heap to quickly find the most recent finished task according to cur task
- use pop out elements to keep recording the previous best result
  - the previous best result is according to cur task (also applicable for future tasks to use)
- push the cur end time and cur result in heap for future tasks
  - when pushing also treat this profit as a candidate of best result
  - we need to keep recording the all time best result

**top k problem (based on heap)**

- heap approach
    - `O(nlogk)`, use heap (size k)
    - `O(n + klogn)`, use heap (size n)
- quick select approach
    - `O(n)` for average and `O(n**2)` for worst
- bucket sort approach
    - `O(n+b)`, bucket (size b)

**k way merge problem**

- maintain heap (size k)
    - when init, often use heapify
    - stored elements must have multiple information inside themself (use tuple)
        - most import information is to record this element is from which way
- each time pop out from heap
    - record if need
    - operate on this way’s element
    - push the new element (same way) in heap

**two heap problem**

- normal two heap
- lazy removal
    - size
    - hashmap

**focus on stored elements**

- use heap to keep elements (min or max group)
- keep store and pop out the invalid elements

**focus on popping out**

- use heap to get the cur min or max element
- contains greedy algorithm’s idea
    - we use popping out to get the most reasonable element to utilize

**use bfs and heap**

- this is one variation of focusing on popping out
- use bfs to find potential valid elements
- use hashset to record visited elements
- use heap to get the cur min or max element