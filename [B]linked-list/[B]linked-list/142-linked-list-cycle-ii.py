# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1, p2 = head, slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
        
# time O(n), due to traverse
# space O(1)
# using linked list and two pointers (slow and fast)
# 2 * (slow) = fast
# 2 * (p + x) = p + x + y + x
# p = y