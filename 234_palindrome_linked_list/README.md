[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)

Given the head of a singly linked list, return true if it is a `palindrome` or false otherwise.

**Example 1:**

![1](image.png)
**Input**
Input: head = [1,2,2,1]
**Output**
Output: true

**Example 2:**

![2](image-1.png)**Input**
Input: head = [1,2]
**Output**
Output: false

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

**Follow-up:** Could you do it in `O(n)` time and `O(1)` space?

```py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tail = self.reverse(slow)

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

    def reverse(self, head: Optional[ListNode]) ->  Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

```
