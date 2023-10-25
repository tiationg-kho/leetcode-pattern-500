# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        height_nodes = defaultdict(list)
        min_height = float('inf')
        max_height = float('-inf')

        def dfs(node):
            nonlocal min_height, max_height
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            cur_height = max(left_height + 1, right_height + 1)
            min_height = min(min_height, cur_height)
            max_height = max(max_height, cur_height)
            height_nodes[cur_height].append(node.val)
            return cur_height

        dfs(root)

        for h in range(min_height, max_height + 1):
            res.append(height_nodes[h][:])
        return res

# time O(n)
# space O(n)
# using tree and dfs (post order and recursive) and hashmap