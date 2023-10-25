# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0, 0)])
        min_col, max_col = 0, 0
        col_rowvals = defaultdict(list)
        while queue:
            node, r, c = queue.popleft()
            min_col, max_col = min(min_col, c), max(max_col, c)
            col_rowvals[c].append((r, node.val))
            if node.left:
                queue.append((node.left, r + 1, c - 1))
            if node.right:
                queue.append((node.right, r + 1, c + 1))
        res = []
        for c in range(min_col, max_col + 1):
            res.append([v for r, v in sorted(col_rowvals[c])])
        return res
    
# time O(n + k * (n/k)log(n/k)), k is the number of cols
# space O(n), due to queue's max size (number of leaf nodes)
# using tree and bfs and hashmap and sort and assign coordinates