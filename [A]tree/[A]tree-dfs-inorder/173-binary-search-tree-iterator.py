# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.node = root

    def next(self) -> int:
        while self.stack or self.node:
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                self.node = self.stack.pop()
                val = self.node.val
                self.node = self.node.right
                return val

    def hasNext(self) -> bool:
        if self.stack or self.node:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# time O(1), due to amortized
# space O(h), only store left nodes, so stack's size is tree height
# using tree and dfs (inorder and iterative) and stack to store the left nodes