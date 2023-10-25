# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first_wrong = None
        second_wrong = None
        prev = None
        cur = root

        def check():
            nonlocal first_wrong, second_wrong, prev, cur
            if prev and prev.val > cur.val:
                if not first_wrong:
                    first_wrong = prev
                second_wrong = cur
            prev = cur

        while cur:
            if not cur.left:
                check()
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    check()
                    pred.right = None
                    cur = cur.right

        first_wrong.val, second_wrong.val = second_wrong.val, first_wrong.val

# time O(n), due to traverse
# space O(1)
# using tree and dfs (inorder and morris traverse)
'''
1. normal morris traversal
2. when have to add to list (not actually add), use prev_node to record
3. next time need to add to list (not actually add), take the prev_node to compare
4. there can have one pair error or two pairs error, so keep the first met error node and last met error node
'''