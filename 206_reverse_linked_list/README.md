[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

**Input:** head = [1,2]
**Output:** [2,1]

**Example 3:**

**Input:** head = []
**Output:** []

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

[206. Обратно связанный список](https://leetcode.com/problems/reverse-linked-list/)

Дав «голову» односвязного списка, переверните список и верните _обратный список_.

**Пример 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Вход:** head = [1,2,3,4,5]
**Выход:** [5,4,3,2,1]

**Пример 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

**Вход:** head = [1,2]
**Выход:** [2,1]

**Пример 3:**

**Вход:** head = []
**Выход:** []

**Ограничения:**

- Количество узлов в списке находится в диапазоне `[0, 5000]`.

- `-5000 <= Node.val <= 5000`

**Продолжение:** Связанный список можно обратить либо итеративно, либо рекурсивно. Можете ли вы реализовать оба варианта?

Решение с помощью цикла:

Идея в том, чтобы последовательно менять связи в списке с каждой итерацией - то есть связывать текущего элемента с предыдущим - указатель на следующий элемент текущего элемента будет на предыдущий элемент.

Создадим 2 указателя - на начало списка (curr) и на предыдущий элемент (prev), который по умолчанию пустой (так как он будет присвоен как next первому элементу, который станет в итоге последним, а последний элемент в связном списке ссылается на пустое значение - null).

Далее выполняем цикл до тех пор, пока curr не равен null:

- для начала сохраняем во временной переменной next указатель curr на следующий элемент в списке (curr.next)
- далее присваиваем curr.next prev, так как мы разворачиваем список, то следующим элементом у текущего должен стать предыдущий (связываем текущий с предыдущим)
- присваиваем prev текущий элемент curr
- обновляем curr - curr = next

```typescript
function reverseList(head: ListNode | null): ListNode | null {
  let curr = head;
  let prev = null;

  while (curr != null) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
}
```

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
```

```go

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var curr *ListNode
    var prev *ListNode
    curr = head

    for curr != nil {
        temp := curr.Next
        curr.Next = prev
        prev = curr
        curr = temp
    }

    return prev
}

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
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;

        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
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
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = 0;

        while (curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
};

```

```rs

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;

        while let Some(mut node) = curr  {
            curr = node.next;

            node.next = prev;

            prev = Some(node);
        }

        return prev;
    }
}

```
