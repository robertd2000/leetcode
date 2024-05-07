from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Double a Number Represented as a Linked List
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        carry = 0

        while head:
            stack.append(head)
            head = head.next

        tail = None

        while stack:
            cur = stack.pop()
            val = cur.val * 2

            if val >= 10:
                val = val % 10
                cur.val = val + carry
                carry = 1
            else:
                cur.val = val + carry
                carry = 0

            cur.next = tail
            tail = cur
        
        if carry:
            temp = tail
            tail = ListNode(carry)
            tail.next = temp

        return tail
