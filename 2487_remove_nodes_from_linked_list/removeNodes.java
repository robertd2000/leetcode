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
    public ListNode reverse(ListNode head) {
        ListNode tail = null;

        while (head != null) {
            ListNode next = head.next;
            head.next = tail;
            tail = head;
            head = next;
        }

        return tail;
    }
    public ListNode removeNodes(ListNode head) {
        ListNode current = reverse(head);
        ListNode tail = current;
        int max = current.val;

        while (current.next != null ){
            if (current.next.val < max) {
                current.next = current.next.next;
            } else {
                current = current.next;
                max = current.val;
            }
        }

        return reverse(tail);
    }
}