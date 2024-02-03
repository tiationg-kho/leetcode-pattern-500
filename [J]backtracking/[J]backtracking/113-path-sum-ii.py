# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []

        def dfs(path, total, node):
            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path[:])
                return
            for child in [node.left, node.right]:
                if child:
                    path.append(child.val)
                    dfs(path, total + child.val, child)
                    path.pop()
        
        if root:
            dfs([root.val], root.val, root)
        return res
        
# time O(n**2), traversal costs O(n) and every leaf performs O(n) to append path to res
# space O(n**2), due to output list
# using dfs and backtracking and backtracking with constraints