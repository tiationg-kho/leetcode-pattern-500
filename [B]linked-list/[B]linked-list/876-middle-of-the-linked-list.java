/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode middleNode(ListNode head) {
      ListNode slow = head;
      ListNode fast = head;
      while (fast != null && fast.next != null) {
          slow = slow.next;
          fast = fast.next.next;
      }
      return slow;
  }
}

// time O(n), due to traverse
// space O(1)
// using linked list and two pointers (slow and fast)
/*
1. If there are two middle nodes, return the second middle node: use 'while fast and fast.next'
2. If there are two middle nodes, return the first middle node: use 'while fast.next and fast.next.next'
*/