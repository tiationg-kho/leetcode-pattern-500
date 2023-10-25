# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        col_vals = defaultdict(list)
        min_col = float('inf')
        max_col = float('-inf')
        while queue:
            node, col = queue.popleft()
            col_vals[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        res = []
        for col in range(min_col, max_col + 1):
            res.append(col_vals[col][:])
        return res

# time O(n), due to traverse
# space O(n), due to hashmap
# using tree and bfs and hashmap and assign coordinates