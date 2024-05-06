# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
            currentNext = head.next
            head.next = tail
            tail = head
            head = currentNext
        return tail

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = tail = self.reverseLinkedList(head)
        currentMax = current.val

        while current.next:
            if current.next.val < currentMax:
                current.next = current.next.next
            else:
                current = current.next
                currentMax = current.val

        return self.reverseLinkedList(tail)