[876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Given the `head` of a singly linked list, return *the middle node of the linked list*.

If there are two middle nodes, return **the second middle** node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

**Input:** head = [1,2,3,4,5]
**Output:** [3,4,5]
**Explanation:** The middle node of the list is node 3.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

**Input:** head = [1,2,3,4,5,6]
**Output:** [4,5,6]
**Explanation:** Since the list has two middle nodes with values 3 and 4, we return the second one.

**Constraints:**

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

[876. Середина связанного списка](https://leetcode.com/problems/middle-of-the-linked-list/)

Для заданной `головы` односвязного списка вернуть *средний узел связанного списка*.

Если есть два средних узла, вернуть **второй средний** узел.

**Пример 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

**Вход:** head = [1,2,3,4,5]
**Выход:** [3,4,5]
**Объяснение:** Средний узел списка — это узел 3.

**Пример 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

**Вход:** head = [1,2,3,4,5,6]
**Выход:** [4,5,6]
**Объяснение:** Поскольку в списке есть два средних узла со значениями 3 и 4, мы возвращаем второй.

**Ограничения:**

- Количество узлов в списке находится в диапазоне `[1, 100]`.
- `1 <= Node.val <= 100`

Задачу можно решить несколькими способами.

Можно попробовать в лоб: пройтись по списку и узнать его длину n, а потом пройтись по нему n / 2 раз и вернуть элемент на этой позиции.

Другой способ - нужно вернуть середину, элемент посередине списка, а значит можно сделать 2 указателя: один быстрый, а второй медленный. Быстрый указатель будет перемещаться на 2 элемента за итерацию, а медленный на 1. Когда быстрый указатель достигнет конца списка, медленный будет на середине:

```typescript
function middleNode(head: ListNode | null): ListNode | null {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  return slow;
}
```

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
```

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}
```

```cpp

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }
};

```

```go

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow := head
    fast := head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    return slow
}

```
