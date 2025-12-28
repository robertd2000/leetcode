from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        p1, p2 = headA, headB

        if p1 is None or p2 is None:
            return None

        while p1 is not None and p2 is not None and p1 != p2:
            p1 = p1.next
            p2 = p2.next

            if p1 == p2:
                return p1

            if p1 is None:
                p1 = headB

            if p2 is None:
                p2 = headA

        return p1