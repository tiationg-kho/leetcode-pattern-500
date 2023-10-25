# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_part_old_head = slow

        prev, cur = None, second_part_old_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second_part_new_head = prev

        res = float('-inf')
        p1, p2 = head, second_part_new_head
        while p1 and p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return res
    
# time O(n)
# space O(1)
# using linked lsit and two pointers (utilize symmetry property) (finding middle, reversing, counting)