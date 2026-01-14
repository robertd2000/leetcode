# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        while curr is not None:
            gcd = self.gcd(prev.val, curr.val)
            node = ListNode(gcd, curr)
            prev.next = node
            prev = curr
            curr = curr.next
        
        return head
        
    def gcd(self, a: int, b: int):
        while b != 0:
            a, b = b, a % b

        return a