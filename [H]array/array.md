# array

## array intro

- **array**
    - contiguous in memory
    - if array is circular
        - concatenate two original array to simulate
        - or use mod on idx

## array pattern

- **traverse**
    - most common operation in array
- **use Boyer Moore vote algorithm**
    - can find majority element (not strictly)
        - need validate again if the res is not guaranteed
    - key concepts
        - candidates
        - voting
        - neutralizing
- **use** **reverse technique**
    - if we want to rotate second part of array to front
        1. reverse whole array (use two pointers)
        2. reverse first part (original second part)
        3. reverse second part (original first part)
- **use array to simulate queue**
    - use mod to get the correct idx to put val
    - notice array can also simulate hashmap for counting
- **use cyclic sort**
    - cyclic sort is time `O(n)`, space `O(1)`
        - array’s elements must be in fixed range
    - treat index as a hash key, building some relation between idx and val as mark
        - utilize the property of values are limited in certain range
    - based on mapping relation, we can
        - keep swapping the element to correct idx/location
        - or use negative marking to modify the val in correct idx
        - or build a graph
            - build idx to val edge
                - val become new idx
                    - keep going
            - cause limited range, will generate at least a many to one mapping (cycle exists)
                - like in [1, n] range, and we have n + 1 numbers
                - multi edge go to same node
            - use two pointers (slow and fast) approach to detect cycle (duplicate numbers)
                - cycle’s starting point is the duplicate numbers
- **use finite state machine**
    - when there are only few states/patterns to switch/detect
- **use difference array**
    - can seen as reverse version of prefix technique
    - can perform range updating in `O(1)`
- **count continuous element**
    - like 0 or 1 or - 1
    - or sometimes we need to convert the original element to 0 or 1 or - 1 for counting
- **use Knuth shuffle**
    - traverse from end to start
        - each round, randomly choose a element (from first element to current element )to swap with current element
- **use reservoir sampling**
    - if input is too large to store, then use reservoir sampling
    - if input is a stream which can not be preprocessed, then use reservoir sampling
    - first element 1/1 to be res
        - second element 1/2 to be res
            - third element 1/3 to be res
                - keep going
- **use swap**
    - can achieve certain order for array
- **maintain array's range dynamically**
    - use pointers
        - array start
        - cur visit
        - array end
- **pre-process the array**
    - for handling the error cases

## line sweep intro

- **line sweep**
    - we focus on the interval’s start or end
        - because that is the changing point
    - can solve interval problem
    - can sort the intervals as pre-processing
        - notice the sort’s key
    - intervals’ relation
        - overlap
            - A meet B (depends, can seem as non overlap)
            - A overlap B
            - A is-finished-by B
            - A contains B
            - A starts B
            - A equals B
            - A during B
        - non overlap
            - A before B

## line sweep pattern

- **compare two intervals each round**
    - can use sort as pre-processing
        - simplify the relation types of two intervals
    - sometimes can use greedy’s idea
        - determine the key of sort
        - determine the current best choice
    - if two intervals belongs to two sequences of intervals instead of same sequence
        - use two pointers to track them
            - use greedy’s idea to decide how to move pointer
        - or use heap to put them into same heap and manage them as same sequence
        - besides, notice that we can also divide single sequence to two sequences
            - one sequence contains start times
            - one sequence contains end times
- **use chronological ordering**
    - use heap to keep previous intervals’ states
        - using heap with greedy’s idea
        - the element/state in heap is a tuple
            - like start time, end time, length of interval
    - or just use variable to keep previous intervals’ states
        - should reconstruct intervals first
            - like give start time a positive val, and give end time a negative val

## prefix sum intro

- **prefix sum**
    
    ```python
    # init
    prefix = [0 for _ in range(len(nums) + 1)]
    total = 0
    for i, num in enumerate(nums):
        total += num
        prefix[i + 1] = total
    
    # idx:    0  1  2  3  4
    nums   = [3, 2, 3, 1]
    prefix = [0, 3, 5, 8, 9] # length is len(nums) + 1
    
    # if we want subarray left idx: 2 and right idx: 3 (inclusive)'s prefix
    # use right idx + 1 - left idx
    prefix[3 + 1] - prefix[2]
    ```
    
    - subarray problem related
    - use list to store
        - prefix sum of num
        - prefix product of num
        - prefix sum of sth
            - this some thing usually depends on the problem, and need certain abstract transition
    - if array only contain two values, can think about modifying element
        - like change them into 1 and - 1

## prefix sum pattern

- **use** **standard prefix sum**
    - prefix sum list’s length is n + 1 or n (depends)
- **use hashmap to valid the gap subarray**
    - combine prefix sum and hashmap can help to find out the valid subarray
    - hashmap
        - key is prefix sum or sth derived from prefix sum
        - value can be idx or count (depends)
        - if we are searching a closest target instead of a fixed target
            - then we should use SortedDict and use binary search

## sliding window intro

- **sliding window**
    
    ```python
    # standard
    left = 0
    for right in range(len(nums)):
        UPDATE_STATES # due to right ptr is moving
        while INVALID:
            UPDATE_STATES # due to left ptr is moving
            left += 1
        if VALID:
            RECORD # record cur best res
    
    # type II
    left = 0
    for right in range(len(nums)):
        UPDATE_STATES # due to right ptr is moving
        while VALID:
            RECORD # record cur best res
            UPDATE_STATES # due to left ptr is moving
            left += 1
    ```
    
    - subarray related problem can think about sliding window
    - the idea of sliding window is we believe the best result can get from certain window
        - so we keep moving/generating window, maintaining it valid, and recording the current best result
    - left and right pointers
        - these two pointers define the window’s range (inclusive)
    - steps
        1. update states due to right ptr is moving
            1. using hashmap or some variables
        2. move left ptr to maintain valid
            1. update states due to left ptr is moving
                1. using hashmap or some variables
        3. if valid
            1. record cur best res
    - important elements
        - update states, maintain valid, record result
            - notice these three elements can be arranged depends on the problem
    - maintain valid’s tip
        - the valid factors could include
            - size
            - char’s frequency
            - unique char’s count
            - sum of the current window
        - when we can not find the clear way to validate
            - we should consider enumerate certain things
                - it will help us to define how to maintain valid (when to move left ptr)

## sliding window pattern

- **use standard sliding window**
    - size is fixed or want to get max size of window
- **use type II sliding window**
    - want to get min size of window

## two pointers same direction intro

- **two pointers same direction**
    - left and right pointers

## two pointers same direction pattern

- **use left ptr to record**
    - left ptr can seems as a slow ptr
- **find next permutation**
    1. find first relative small num a in right side (if can not find a, then we are already in the largest permutation)
    2. find first relative large num b (to that relative small num) in right side
    3. swap a and b
    4. let second half subarray (after that swap idx (b's new idx)) become monotonic increasing (reverse them)
- **traverse two sequences**

## two pointers opposite direction intro

two pointers opposite direction

## two pointers opposite direction pattern

- **use shrink type**
    - could use the attribute of sorted order
    - if not sorted
        - we should greedily think move which side’s ptr will be the current best choice
        - or think which side’s ptr’s result is already the final result
            - record it if need, then move this side’s ptr
        - or the both side shrink together
            - sometimes can use when we want to reverse array
- **use expand type**

## sort intro

- **sort**
    - A **stable** sorting algorithm means that when two elements have the same value, their relative order is maintained
    - An **in-place** sorting algorithm means that the algorithm does not use additional data structure to hold temporary data
    - Python uses Timsort, which uses merge sort for larger data and insertion sort for smaller data
    - merge sort
        - involve divide and conquer’s idea
    
    ```python
    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            def merge_sort(nums):
                n = len(nums)
                if n <= 1:
                    return nums
                m = n // 2
                left_part = merge_sort(nums[: m])
                right_part = merge_sort(nums[m:])
                res = []
                left, right = 0, 0
                while left < m or right < n - m:
                    if left == m:
                        res.append(right_part[right])
                        right += 1
                    elif right == n - m:
                        res.append(left_part[left])
                        left += 1
                    elif left_part[left] <= right_part[right]:
                        res.append(left_part[left])
                        left += 1
                    else:
                        res.append(right_part[right])
                        right += 1
                return res
            
            return merge_sort(nums)
    
    # time O(nlogn), logn recursion layers and each layer costs O(n)
    # space O(n), due to new list, recursion stack is O(logn)
    # using merge sort
    # stable
    ```
    
    - quick sort and quick select
        - involve divide and conquer’s idea
    
    ```python
    import random
    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            def quick_sort(left, right):
                if left >= right:
                    return
                pivot_idx = random.randint(left, right)
                pivot_val = nums[pivot_idx]
                nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
                partition_idx = left
                for i in range(left, right):
                    if nums[i] < pivot_val:
                        nums[i], nums[partition_idx] = nums[partition_idx], nums[i]
                        partition_idx += 1
                nums[right], nums[partition_idx] = nums[partition_idx], nums[right]
                quick_sort(left, partition_idx - 1)
                quick_sort(partition_idx + 1, right)
                return
                
            quick_sort(0, len(nums) - 1)
            return nums
        
    # time O(n**2), when the list is almost sorted, and the average time is O(nlogn)
    # space O(n), due to recursion layers, O(logn) in average
    # using quick sort
    # unstable
    
    import random
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            def quick_select(left, right):
                pivot_idx = random.randint(left, right)
                pivot_val = nums[pivot_idx]
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                partition_idx = left
                for i in range(left, right):
                    if nums[i] < pivot_val:
                        nums[i], nums[partition_idx] = nums[partition_idx], nums[i]
                        partition_idx += 1
                nums[partition_idx], nums[right] = nums[right], nums[partition_idx]
                return partition_idx
    
            left, right = 0, len(nums) - 1
            while left <= right:
                idx = quick_select(left, right)
                if idx == len(nums) - k:
                    return nums[idx]
                elif idx > len(nums) - k:
                    right = idx - 1
                else:
                    left = idx + 1
            return None
    
    # time O(n**2) in worst, O(n) in average
    # space O(1)
    # using quick select
    ```
    
    - bucket sort
    
    ```python
    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            min_num = min(nums)
            max_num = max(nums)
            buckets = [0 for _ in range(max_num - min_num + 1)]
            for num in nums:
                buckets[num - min_num] += 1
            res = []
            for i, b in enumerate(buckets):
                if b:
                    res.extend([i + min_num for _ in range(b)])
            return res
        
    # time O(n+b)
    # space O(n+b)
    # using bucket sort
    ```

## sort pattern

- **use self defined sort**
    - merge sort
    - quick sort
- **top k problem (based on sort)**
    - heap
        - `O(nlogk)`, use heap (size k)
        - `O(n + klogn)`, use heap (size n)
    - quick select
        - `O(n)` for average and `O(n**2)` for worst
    - bucket sort
        - `O(n+b)`, bucket (size b)
- **use bucket sort**
    - `O(n+b)`, bucket (size b)
    - involve counting’s idea
    - bucket can contain
        - a value
        - or list of elements
- **use quick select**
    - `O(n)` for average and `O(n**2)` for worst
    - can use to find kth large number
        - like median
- **use merge sort**
    - involve divide and conquer’s idea
