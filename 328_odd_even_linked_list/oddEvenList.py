from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd, even = head, head.next
        even_head = even
        
        while even is not None and even.next is not None:
            odd.next = odd.next.next            
            even.next = even.next.next

            odd = odd.next            
            even = even.next

        
        odd.next = even_head

        return head