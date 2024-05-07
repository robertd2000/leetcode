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
    public ListNode doubleIt(ListNode head) {
        ListNode current = head;
        ListNode prev = null;

        while (current != null) {
            int value = current.val * 2;

            if (value < 10) {
            current.val = value;
            } else if (prev != null) {
                current.val = value % 10;
                prev.val++;
            } else {
                head = new ListNode(1, current);
                current.val = value % 10;
            }

            prev = current;
            current = current.next;
        }

        return head;
    }
}