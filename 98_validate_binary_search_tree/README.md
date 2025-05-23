[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left
  subtree
  of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

**Input:** root = [2,1,3]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`

[98. Проверка двоичного дерева поиска](https://leetcode.com/problems/validate-binary-search-tree/)

Дав «корень» двоичного дерева, _определите, является ли оно допустимым двоичным деревом поиска (BST)_.

**Допустимое BST** определяется следующим образом:

- Левое

поддерево

узла содержит только узлы с ключами **меньше** ключа узла.

- Правое поддерево узла содержит только узлы с ключами **больше** ключа узла.
- И левое, и правое поддеревья также должны быть двоичными деревьями поиска.

**Пример 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

**Вход:** root = [2,1,3]
**Выход:** true

**Пример 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

**Вход:** root = [5,1,4,null,null,3,6]
**Выход:** false
**Объяснение:** Значение корневого узла равно 5, но значение его правого потомка равно 4.

**Ограничения:**

- Количество узлов в дереве находится в диапазоне `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`

Решение с помощью поиска в глубину и проверки значений левого и правого деревьев. Нужно также где-то хранить минимальное и максимальные значение для текущего дерева, например в качестве параметров функции.

Создадим функцию dfs, которая будет принимать корень дерева и минимальное и максимальное значения. Функция будет вызываться рекурсивно для правого и левого деревьев.

Если корень текущего дерева null, то вернем true, так как пустое дерево по умолчанию сбалансировано.

Если значение текущего корня больше либо меньше переданных максимального и минимального значения, то значит дерево не сбалансировано и нужно вернуть false.

Иначе вызовем рекурсивно dfs для левого дерева, передав в качестве максимального значения корень текущего дерева и для правого дерева, передав в качестве минимального значения корень текущего дерева:

```typescript
return dfs(root.left, minVal, root.val) && dfs(root.right, root.val, maxVal);
```

То есть для левого дерева мы передаем текущий корень в качестве максимального значения, так как ни один элемент слева не может быть больше корня. Аналогично с правым деревом: передается корень как минимальное значение , так как все элементы справа должны быть больше чем корень.

Итоговый код:

```typescript
function isValidBST(root: TreeNode | null): boolean {
  return dfs(root, -Infinity, Infinity);
}

function dfs(root: TreeNode | null, minVal: number, maxVal: number) {
  if (root == null) return true;

  if (root.val <= minVal || root.val >= maxVal) return false;

  return dfs(root.left, minVal, root.val) && dfs(root.right, root.val, maxVal);
}
```

![[Pasted image 20240628141708.png]]

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -pow(2, 31) - 1, pow(2, 31) + 1)

    def dfs(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if root is None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.dfs(root.left, minVal, root.val) and self.dfs(
            root.right, root.val, maxVal
        )
```

```go

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	return dfs(root, math.MinInt, math.MaxInt)
}

func dfs(root *TreeNode, minVal int, maxVal int) bool {
	if root == nil {
		return true
	}

	if root.Val <= minVal || root.Val >= maxVal {
		return false
	}

	return dfs(root.Left, minVal, root.Val) && dfs(root.Right, root.Val, maxVal)
}
```

```rs

use std::rc::Rc;
use std::cell::RefCell;
type OptNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn is_valid_bst(root: OptNode) -> bool {
        Self::is_valid(&root, i32::MIN as i64 - 1, i32::MAX as i64 + 1)
    }

    fn is_valid(node: &OptNode, gt: i64, lt: i64) -> bool {
        match node.as_ref() {
            None => true,
            Some(n) => {
                let b = n.borrow();
                (b.val as i64) > gt && (b.val as i64) < lt
                    && Self::is_valid(&b.left, gt, b.val as i64)
                    && Self::is_valid(&b.right, b.val as i64, lt)
            }
        }
    }
}
```

```java

class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean valid(TreeNode node, long minimum, long maximum) {
        if (node == null) return true;

        if (!(node.val > minimum && node.val < maximum)) return false;

        return valid(node.left, minimum, node.val) && valid(node.right, node.val, maximum);
    }
}

```

```cpp

class Solution {
public:
    bool isValidBST(TreeNode* root) { return valid(root, LONG_MIN, LONG_MAX); }

private:
    bool valid(TreeNode* node, long minimum, long maximum) {
        if (!node)
            return true;

        if (!(node->val > minimum && node->val < maximum))
            return false;

        return valid(node->left, minimum, node->val) &&
               valid(node->right, node->val, maximum);
    }
};

```
