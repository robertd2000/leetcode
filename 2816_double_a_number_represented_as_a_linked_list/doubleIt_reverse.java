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
            ListNode currentNext = head.next;
            head.next = tail;
            tail = head;
            head = currentNext;
        }

        return tail;
    }

    public ListNode doubleIt(ListNode head) {
        ListNode current = reverse(head);
        ListNode tail = current;
        int carry = 0;


        while (current != null) {
            int value = current.val * 2;

            if (value >= 10) {
                value = value % 10;
                current.val = value + carry;
                carry = 1;
            } else {
                current.val = value + carry;
                carry = 0;
            }

            current = current.next;
        } 


        tail = reverse(tail);

        if (carry > 0) {
            tail = new ListNode(carry, tail);
        }

        return tail;
    }
}