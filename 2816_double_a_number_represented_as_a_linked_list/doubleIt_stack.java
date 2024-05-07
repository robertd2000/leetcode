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
        Deque<ListNode> stack = new ArrayDeque<>();
        int carry = 0;

        while (head != null) {
            stack.push(head);
            head = head.next;
        }

        ListNode tail = null;
        while (!stack.isEmpty()) {
            ListNode current = stack.pop();
            int value = current.val * 2;

            if (value >= 10) {
                value = value % 10;
                current.val = value + carry;
                carry = 1;
            } else {
                current.val = value + carry;
                carry = 0;
            }

            current.next = tail;
            tail = current;
        }

        if (carry > 0) {
            tail = new ListNode(carry, tail);
        }

        return tail;
    }
}