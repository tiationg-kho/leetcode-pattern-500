# binary search

## intro

```python
# approach 1
# search in a sorted array for specific val
# or search in sth’s range
class Solution:
    def binary_search(self, nums, TARGET):
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] > TARGET:
                right = m - 1
            elif nums[m] == TARGET:
                boundary = m
                break
            else:
                left = m + 1
        return boundary
```

```python
# approach 2
# search in a sorted array for most close val to specific val
# or search in sth’s range
class Solution:
    def binary_search(self, nums, LIMIT):
        left, right, boundary = LOW_BOUND, UP_BOUND, - 1
        
        def valid(PARAMETERS):
            SOME OPS DUE TO LIMIT
            return BOOL
        
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1 # or left = m + 1
            else:
                left = m + 1 # or right = m - 1
        return boundary
```

- an efficient sorted array search algorithm
    - can search for specific val
    - can search for most close val to specific val
    - can make a binary decision to shrink the search range
- time `O(log(n))`, space `O(1)`
- left and right can be a range from
    - sorted array’s start and end
    - sth’s low_bound and up_bound
- use a boundary (ptr) to record the current best/valid answer, then try to get better one

## pattern

**search in a sorted array for specific val**

- when shrinking, will have 3 logic branch mostly

**search in a sorted array for most close val**

- when shrinking, will have 2 logic branch mostly

**search in sth’s range**

- search between sth’s low_bound and up_bound
    - num
    - length
    - capacity
    - distance
    - total
    - sum
    - cost
- can be for specific val or for most close val. mostly for most close val

**use boundary to record**

- depends on different condition, binary search could have different logic branch, and only inside certain branch could record the boundary
- when recording, we should consider the concept of greedy algorithm
- implement
    - use - 1 to initiation, to handle not find situation
        - inside branch, record most valid answer in cur condition
    - or use len(nums) - 1 to initiation, as a potential valid answer
        - inside branch, record most valid answer in cur condition
    - or doesn’t need it, when it is guaranteed to have a specific answer

**rotated sorted array**

- use mid ptr to compare to right ptr (help us to know which side of mid ptr can treat as sorted)
    - if mid ptr val larger than right ptr val, means the left side of mid ptr has order
    - if mid ptr val less than right ptr val, means the right side of mid ptr has order
    - then figure out our target val is
        1. between left and mid (ascending order)
        2. not between left and mid (not sure)
        3. between mid and right (ascending order)
        4. not between mid and right (not sure)
    - notice: above approach is based on the array only contain unique vals
        - if contain duplicate vals, when the mid == right (means cannot decide which side could be sorted), we can only wipe out this one element in this round