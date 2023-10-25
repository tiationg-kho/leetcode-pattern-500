# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def build(node):
            if not node:
                return '#null'
            cur = '#' + str(node.val)
            left = build(node.left)
            right = build(node.right)
            return cur + left + right

        tree = build(root)
        subtree = build(subRoot)

        base = 131
        mod = 10 ** 9 + 7
        val = 0

        for i, c in enumerate(subtree):
            val = (val * base + ord(c)) % mod

        target_val = val
        val = 0
        remove_val = (base ** (len(subtree) - 1)) % mod
        for i, c in enumerate(tree):
            if i < len(subtree):
                val = (val * base + ord(c)) % mod
                if i == len(subtree) - 1:
                    if val == target_val:
                        return True
            else:
                val -= (remove_val * ord(tree[i - len(subtree)])) % mod
                val = (val * base + ord(c)) % mod
                if val == target_val:
                    return True
        return False

# time O(n+m)
# space O(n+m)
# using tree and dfs (preorder and recursive) and turn tree to string and rabin karp (rolling hash)