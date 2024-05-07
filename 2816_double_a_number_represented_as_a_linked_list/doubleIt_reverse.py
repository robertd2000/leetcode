# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Double a Number Represented as a Linked List     
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
            currentNext = head.next
            head.next = tail
            tail = head
            head = currentNext

        return tail

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = tail = self.reverse(head)
        carry = 0
        
        while current:
            val = current.val * 2
            if val >= 10:
                val = val % 10
                current.val = val + carry
                carry = 1
            else:
                current.val = val + carry
                carry = 0
            current = current.next

        tail = self.reverse(tail)
        
        if carry:
            temp = tail
            tail = ListNode(carry)
            tail.next = temp

        return tail