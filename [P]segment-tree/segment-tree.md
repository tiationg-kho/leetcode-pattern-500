# segment tree

## intro
| Aspect              | Prefix Sum                               | Difference Array                               | Segment Tree                                                  |
| ------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| **Primary Purpose** | range sum queries                        | range updates                                  | range queries, and range updates                              |
| **Operation Time**  | Sum Query: `O(1)`                        | Update: `O(1)`                                 | Query: `O(logC)` or `O(logn)`; Update: `O(logC)` or `O(logn)` |
| **Reconstruction**  | get original array from diff of elements | get original array from prefix sum of elements | N/A                                                           |
| **Use Case**        | static arrays                            | cumulative updates                             | interval-based manipulations                                  |
- segment tree is a tree where each node is an interval
- tree based is more easy to understand
- build tree `O(n)`
    - or use dynamic build, only build node when update() and query(), cost `O(logC)` (C is max val of num we assign)
- point modify `O(logC)` or `O(logn)`
- range query `O(logC)` or `O(logn)`
    - sum
    - count
    - max
    - other related aggregations
- range modify `O(logC)` if using lazy propagation
    - can have multiple lazy variables depends on how many operations need
- push_down(), push_up(), update(), query() will be implemented differently depends on the diff type of range query and range modify

```python
# sum type
# non dynamic build
# non range modification
# non lazy propagation
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = None
        self.right = None
        self.val = 0

class SegmentTree:
    def __init__(self, nums):
        def build(start, end):
            if start == end:
                node = Node(start, end)
                node.val = nums[start]
                return node
            node = Node(start, end)
            node.left = build(start, node.mid)
            node.right = build(node.mid + 1, end)
            node.val = node.left.val + node.right.val
            return node
        
        self.root = build(0, len(nums) - 1)
    
    def update(self, index, val):
        def helper(node, index, val):
            if node.start == node.end:
                node.val = val
                return 
            if index <= node.mid:
                helper(node.left, index, val)
            else:
                helper(node.right, index, val)
            node.val = node.left.val + node.right.val
        
        helper(self.root, index, val)

    def query(self, left, right):
        def helper(node, start, end):
            if start <= node.start and node.end <= end:
                return node.val
            res = 0
            if start <= node.mid:
                res += helper(node.left, start, end)
            if end >= node.mid + 1:
                res += helper(node.right, start, end)
            return res
            
        return helper(self.root, left, right)

# time O(n) for initialize and O(logn) for update() and query()
# space O(n), due to segment tree
# using segment tree and sum type segment tree
```

```python
# sum type
# with dynamic build
# with range modification
# with lazy propagation
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0

class SegmentTree:
    def __init__(self, start, end):
        self.root = Node(start, end)

    def push_down(self, node):
        if not node.left:
            node.left = Node(node.start, node.mid)
        if not node.right:
            node.right = Node(node.mid + 1, node.end)
        if node.lazy == 0:
            return
        node.left.val += node.lazy * (node.left.end - node.left.start + 1)
        node.right.val += node.lazy * (node.right.end - node.right.start + 1)
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0

    def push_up(self, node):
        node.val = node.left.val + node.right.val

    def update(self, node, start, end, add):
        if start <= node.start and node.end <= end:
            node.val += add * (node.end - node.start + 1)
            node.lazy += add
            return
        self.push_down(node)
        if start <= node.mid:
            self.update(node.left, start, end, add)
        if end >= node.mid + 1:
            self.update(node.right, start, end, add)
        self.push_up(node)

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val
        self.push_down(node)
        res = 0
        if start <= node.mid:
            res += self.query(node.left, start, end)
        if end >= node.mid + 1:
            res += self.query(node.right, start, end)
        return res

# time O(1) for initialize and O(logC) for others
# space O(min(n, C)), due to segment tree
# using segment tree and sum type segment tree
```

## pattern
- use sum type segment tree
- use count type segment tree
- use max type segment tree
