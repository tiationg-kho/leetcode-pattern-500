# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def dfs(path, node):
            if not node.left and not node.right:
                res.append('->'.join(path))
                return
            for child in [node.left, node.right]:
                if child:
                    path.append(str(child.val))
                    dfs(path, child)
                    path.pop()
        
        if root:
            dfs([str(root.val)], root)
        return res
    
# time O(n**2)
# space O(n**2)
# using dfs and backtracking and backtracking with constraints