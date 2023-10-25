# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(next=head)
        interval_len = 1
        while interval_len < count:
            new_list = dummy
            cur = dummy.next
            while cur:
                interval1_len = 0
                interval1 = cur
                while cur and interval1_len < interval_len:
                    interval1_len += 1
                    cur = cur.next
                interval2_len = 0
                interval2 = cur
                while cur and interval2_len < interval_len:
                    interval2_len += 1
                    cur = cur.next
                while interval1_len or interval2_len:
                    if (interval1_len and interval2_len and interval1.val < interval2.val) or (interval2_len == 0):
                        new_list.next = interval1
                        new_list = new_list.next
                        interval1 = interval1.next
                        interval1_len -= 1
                    else:
                        new_list.next = interval2
                        new_list = new_list.next
                        interval2 = interval2.next
                        interval2_len -= 1
            new_list.next = None
            interval_len *= 2
        return dummy.next
                    
# time O(nlogn), due to merge sort
# space O(1)
# using linked list and iterative merge sort (bottom up)