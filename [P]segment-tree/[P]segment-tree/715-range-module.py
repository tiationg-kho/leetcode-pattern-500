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
            return
        self.push_down(node)
        if start <= node.mid:
            self.update(node.left, start, end, val)
        if end >= node.mid + 1:
            self.update(node.right, start, end, val)
        self.push_up(node)

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val == node.end - node.start + 1
        self.push_down(node)
        if start <= node.mid:
            if not self.query(node.left, start, end):
                return False
        if end >= node.mid + 1:
            if not self.query(node.right, start, end):
                return False
        return True

class RangeModule:

    def __init__(self):
        self.st = SegmentTree(0, 10**9)

    def addRange(self, left: int, right: int) -> None:
        self.st.update(self.st.root, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(self.st.root, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(self.st.root, left, right - 1, 0)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# time O(1) for initialize and O(logC) for others
# space O(min(n, C)), due to segment tree
# using segment tree and count type segment tree