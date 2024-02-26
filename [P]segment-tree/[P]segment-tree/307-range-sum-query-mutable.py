class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = None
        self.right = None
        self.val = 0

class NumArray:
    def __init__(self, nums: List[int]):
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
    
    def update(self, index: int, val: int) -> None:
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

    def sumRange(self, left: int, right: int) -> int:
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

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# time O(n) for initialize and O(logn) for update() and sumRange()
# space O(n), due to segment tree
# using segment tree and sum type segment tree