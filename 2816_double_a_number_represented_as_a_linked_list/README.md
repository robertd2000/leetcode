# [2816. Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07)

You are given the `head` of a **non-empty** linked list representing a non-negative integer without leading zeroes.

Return _the `head` of the linked list after **doubling** it._

## Example 1:

![1](image.png)

```

Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

```

## Example 2:

![2](image-1.png)

```

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

```

## Constraints:

- The number of nodes in the list is in the range `[1, 104]`
- `0 <= Node.val <= 9`
- The input is generated such that the list represents a number that does not have leading zeros, except the number `0` itself.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)` (stack) / `O(1)`

# Code

**Stack** (with extra space)

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        carry = 0

        current = head

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


```

```java

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

```

**Reverse** (without using extra-space)

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

```

```java

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

```

**One iteration**

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)

        node = head

        while node:
            node.val = (node.val * 2) % 10

            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next

        return head

```

```java

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
        if (head.val > 4) {
            head = new ListNode(0, head);
        }

        ListNode node = head;

        while (node != null) {
            node.val = (node.val * 2) % 10;
            if (node.next != null && node.next.val > 4) {
                node.val += 1;
            }

            node = node.next;
        }

        return head;
    }
}

```

**Two Pointers**

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

```

```java

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
        ListNode current = head;
        ListNode prev = null;

        while (current != null) {
            int value = current.val * 2;

            if (value < 10) {
            current.val = value;
            } else if (prev != null) {
                current.val = value % 10;
                prev.val++;
            } else {
                head = new ListNode(1, current);
                current.val = value % 10;
            }

            prev = current;
            current = current.next;
        }

        return head;
    }
}

```
