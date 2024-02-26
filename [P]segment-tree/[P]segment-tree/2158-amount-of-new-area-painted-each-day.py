class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = - 1

class SegmentTree:
    def __init__(self, start, end):
        self.root = Node(start, end)

    def push_down(self, node):
        if not node.left:
            node.left = Node(node.start, node.mid)
        if not node.right:
            node.right = Node(node.mid + 1, node.end)
        if node.lazy == - 1:
            return
        node.left.val = node.lazy * (node.left.end - node.left.start + 1)
        node.right.val = node.lazy * (node.right.end - node.right.start + 1)
        node.left.lazy = node.lazy
        node.right.lazy = node.lazy
        node.lazy = - 1

    def push_up(self, node):
        node.val = node.left.val + node.right.val

    def update(self, node, start, end, val):
        if start <= node.start and node.end <= end:
            node.val = val * (node.end - node.start + 1)
            node.lazy = val
            return node.val
        self.push_down(node)
        res = 0
        if start <= node.mid:
            res += self.update(node.left, start, end, val)
        if end >= node.mid + 1:
            res += self.update(node.right, start, end, val)
        self.push_up(node)
        return res

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

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        st = SegmentTree(0, 10**9)
        res = []
        for p, q in paint:
            s, e = p, q - 1
            old_paint = st.query(st.root, s, e)
            new_paint = st.update(st.root, s, e, 1)
            res.append(new_paint - old_paint)
        return res

# time O(nlogC)
# space O(n), due to segment tree
# using segment tree and count type segment tree