# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        cur = head

        def build_helper(left, right):
            nonlocal cur
            if left > right:
                return None

            mid = (left + right) // 2
            left_subtree = build_helper(left, mid - 1)

            node = TreeNode(cur.val)
            cur = cur.next

            node.left = left_subtree

            right_subtree = build_helper(mid + 1, right)
            node.right = right_subtree
            return node

        return build_helper(0, count - 1)
    
# time O(n)
# space O(logn), due to recursion stack
# using tree and divide and conquer and re-build BST (inorder approach)
'''
1. use divide and conquer, simulate inorder traversal
2. follow linked list ptr, so build left tree first then root then right tree
'''