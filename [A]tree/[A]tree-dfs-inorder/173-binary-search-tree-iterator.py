# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        res = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return res

    def hasNext(self) -> bool:
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# time O(1), due to amortized, initiation is O(h)
# space O(h), only store left nodes, so stack's size is tree height
# using tree and dfs (inorder and iterative) and stack to store the left nodes