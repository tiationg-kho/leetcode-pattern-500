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
        node.left.val = max(node.left.val, node.lazy)
        node.right.val = max(node.right.val, node.lazy)
        node.left.lazy = max(node.left.lazy, node.lazy)
        node.right.lazy = max(node.right.lazy, node.lazy)
        node.lazy = 0

    def push_up(self, node):
        node.val = max(node.left.val, node.right.val)

    def update(self, node, start, end, val):
        if start <= node.start and node.end <= end:
            node.val = max(node.val, val)
            node.lazy = max(node.lazy, val)
            return
        self.push_down(node)
        if start <= node.mid:
            self.update(node.left, start, end, val)
        if end >= node.mid + 1:
            self.update(node.right, start, end, val)
        self.push_up(node)

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val
        self.push_down(node)
        res = 0
        if start <= node.mid:
            res = max(res, self.query(node.left, start, end))
        if end >= node.mid + 1:
            res = max(res, self.query(node.right, start, end))
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        st = SegmentTree(0, 10**9)
        res = 0
        for num in nums:
            prev_len = st.query(st.root, max(num - k, 0), num - 1)
            cur_len = prev_len + 1
            st.update(st.root, num, num, cur_len)
            res = max(res, cur_len)
        return res
            
# time O(nlogC)
# space O(n), due to segment tree
# using segment tree and max type segment tree