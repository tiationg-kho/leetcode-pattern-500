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
        node.left.val += node.lazy
        node.right.val += node.lazy
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0

    def push_up(self, node):
        node.val = max(node.left.val, node.right.val)

    def update(self, node, start, end, val):
        if start <= node.start and node.end <= end:
            node.val += val
            node.lazy += val
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

class MyCalendarTwo:

    def __init__(self):
        self.st = SegmentTree(0, 10**9)

    def book(self, start: int, end: int) -> bool:
        if self.st.query(self.st.root, start, end - 1) == 2:
            return False
        self.st.update(self.st.root, start, end - 1, 1)
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

# time O(1) for initialize and O(logC) for book and others
# space O(min(n, C)), due to segment tree
# using segment tree and max type segment tree