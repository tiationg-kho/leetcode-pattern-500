# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def inorder_helper(root):
            if not root:
                return
            inorder_helper(root.left)
            inorder.append(root.val)
            inorder_helper(root.right)
        inorder_helper(root)
        return inorder
    
# time O(n), due to traverse
# space O(n), due to memory stack
# using tree and dfs (inorder and recursive)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        if not root:
            return inorder
        node = root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
        return inorder

# time O(n), due to traverse
# space O(n), due to stack
# using tree and dfs (inorder and iterative)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
				inorder = []
		    if not root:
		        return inorder
		    stack = [(root, False)]
		    while stack:
		        node, children_visited = stack.pop()
		        if children_visited:
		            inorder.append(node.val)
		        else:
		            if node.right:
		                stack.append((node.right, False))
		            stack.append((node, True))
		            if node.left:
		                stack.append((node.left, False))
		    return inorder

# time O(n), due to traverse
# space O(n), due to stack
# using tree and dfs (inorder and iterative)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        cur = root
        while cur:
            if not cur.left:
                inorder.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    inorder.append(cur.val)
                    prev.right = None
                    cur = cur.right
        return inorder
        
# time O(n), due to traverse
# space O(1), if don't count output list
# using tree and dfs (inorder and morris traversal)