from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None

        while current:
            val = current.val * 2

            if val < 10:
                current.val = val
            elif prev:
                current.val = val % 10
                prev.val += 1
            else:
                head = ListNode(1, current)
                current.val = val % 10

            prev = current
            current = current.next

        return head