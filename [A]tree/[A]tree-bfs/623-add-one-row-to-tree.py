# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
            
        if depth == 1:
            return TreeNode(val=val, left=root)

        queue = deque([(root, 1)])
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node, level = queue.popleft()
                if level == depth - 1:
                    node.left = TreeNode(val=val, left=node.left)
                    node.right = TreeNode(val=val, right=node.right)
                else:
                    for child in [node.left, node.right]:
                        if child:
                            queue.append((child, level + 1))
        return root
    
# time O(n)
# space O(n)
# using tree and bfs