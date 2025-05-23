[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

Given a binary tree, determine if it is

**height-balanced**

.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**Input:** root = [3,9,20,null,null,15,7]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**Input:** root = [1,2,2,3,3,null,null,4,4]
**Output:** false

**Example 3:**

**Input:** root = []
**Output:** true

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-104 <= Node.val <= 104`

[110. Сбалансированное двоичное дерево](https://leetcode.com/problems/balanced-binary-tree/)

Для заданного двоичного дерева определите, является ли оно

**сбалансированным по высоте**

.

**Пример 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**Вход:** root = [3,9,20,null,null,15,7]
**Выход:** true

**Пример 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**Вход:** root = [1,2,2,3,3,null,null,4,4]
**Выход:** false

**Пример 3:**

**Вход:** root = []
**Выход:** true

**Ограничения:**

- Количество узлов в дереве находится в диапазоне `[0, 5000]`.

- `-104 <= Node.val <= 104`

Для решения данной задачи нужно использовать рекурсию и поиск в глубину. Создадим вспомогательную функцию getHeight, которая будет принимать root и возвращать высоту. Если root равен null, то высота равна 0, так как нет дочерних элементов, поэтому вернем 0.

```typescript
if (root === null) return 0;
```

Далее нужно рассчитать высоту левого и правого поддеревьев:

```typescript
const leftHeight = getHeight(root.left);
const rightHeight = getHeight(root.right);
```

В итоге нужно вернуть максимальное из левого и правого поддеревьев:

```typescript
return Math.max(leftHeight, rightHeight) + 1;
```

Таким образом с помощью getHeight мы рассчитываем высоту дерева.

Рассчитаем высоту правого и левого поддеревьев с помощью getHeight:

```typescript
const left = getHeight(root.left);
const right = getHeight(root.right);
```

Узнаем разницу высот полученных деревьев:

```typescript
const skew = Math.abs(left - right);
```

Если больше 1, то дерево не сбалансированно.

Но нужно также проверить что все деревья в этом дереве тоже сбалансированы, для этого нужно вызвать isBalanced для левого и правого поддерева:

```typescript
return skew <= 1 && isBalanced(root.left) && isBalanced(root.right);
```

```typescript
function isBalanced(root: TreeNode | null): boolean {
  if (root === null) return true;

  const left = getHeight(root.left);
  const right = getHeight(root.right);

  const skew = Math.abs(left - right);

  return skew <= 1 && isBalanced(root.left) && isBalanced(root.right);
}

function getHeight(root: TreeNode | null): number {
  if (root === null) return 0;

  const leftHeight = getHeight(root.left);
  const rightHeight = getHeight(root.right);

  return Math.max(leftHeight, rightHeight) + 1;
}
```

Вместо вызова isBalanced рекурсивно можно сделать глобальную переменную balanced и проверять разницу между высотами правого и левого деревьев:

```typescript
function isBalanced(root: TreeNode | null): boolean {
  if (root === null) return true;

  let balanced = true;

  function getHeight(root: TreeNode | null): number {
    if (root === null) return 0;

    const leftHeight = getHeight(root.left);

    if (balanced === false) {
      return 0;
    }
    const rightHeight = getHeight(root.right);

    const skew = Math.abs(leftHeight - rightHeight);

    if (skew > 1) {
      balanced = false;
      return 0;
    }
    return Math.max(leftHeight, rightHeight) + 1;
  }

  getHeight(root);

  return balanced;
}
```

```py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            left = self.getHeight(root.left, 0)
            right = self.getHeight(root.right, 0)

            skew = abs(left - right)

            return skew <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        return True


    def getHeight(self, root, height):
        if not root:
            return 0
        lHeight = self.getHeight(root.left, height)
        rHeight = self.getHeight(root.right, height)

        return max(lHeight, rHeight) + 1


```

```py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ERR_CODE = -sys.maxsize - 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._get_height(root) != ERR_CODE

    def _get_height(self, root: TreeNode) -> int:
        if root:
            left = self._get_height(root.left)
            if left == ERR_CODE:
                return ERR_CODE
            right = self._get_height(root.right)
            if right == ERR_CODE:
                return ERR_CODE
            diff = abs(left - right)
            if diff > 1:
                return ERR_CODE
            return max(left, right) + 1

        return 0

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
func isBalanced(root *TreeNode) bool {
	if root != nil {
		left := getHeight(root.Left)
		right := getHeight(root.Right)
		skew := abs(left, right)

		if !isBalanced(root.Left) {
			return false
		}
		if !isBalanced(root.Right) {
			return false
		}
		if skew > 1 {
			return false
		}

		return true
	}

	return true
}

func getHeight(root *TreeNode) int {
	if root != nil {
		left := getHeight(root.Left)
		right := getHeight(root.Right)

		return max(left, right) + 1
	}

	return 0
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func abs(a, b int) int {
	c := a - b
	if c < 0 {
		return -c
	}

	return c
}


```

```java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;

        int left = getHeight(root.left);
        int right = getHeight(root.right);

        int skew = Math.abs(left - right);

        if (!isBalanced(root.left)) return false;
        if (!isBalanced(root.right)) return false;
        if (skew > 1) return false;

        return true;
    }

    private int getHeight(TreeNode root) {
        if (root == null) return 0;

        int left = getHeight(root.left);
        int right = getHeight(root.right);

        return Math.max(left, right) + 1;
    }
}

```

```cpp

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root) {
            int left = getHeight(root->left);
            int right = getHeight(root->right);
            int skew = abs(left - right);

            if (!isBalanced(root->left)) return false;
            if (!isBalanced(root->right)) return false;
            if (skew > 1) return false;

            return true;
        }
        return true;
    }

    int getHeight(TreeNode* root) {
        if (root == 0) return 0;

        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);

        return max(leftHeight, rightHeight) + 1;
    }
};

```

```rs

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::cmp;

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if let Some(node) = root {
            let right = node.borrow().right.clone();
            let left = node.borrow().left.clone();
            let left_val = Solution::get_height(left.clone());
            let right_val = Solution::get_height(right.clone());

            let skew = (left_val - right_val).abs();

            if skew > 1 {
                return false;
            }

            if !Solution::is_balanced(left) {
                return false;
            }

            if !Solution::is_balanced(right) {
                return false;
            }

            return true;
        }

        return true;
    }

    pub fn get_height(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(node) = root {
            let right = node.borrow().right.clone();
            let left = node.borrow().left.clone();
            let left_val = Solution::get_height(left);
            let right_val = Solution::get_height(right);

            return cmp::max(left_val, right_val) + 1;
        } else {
            return 0;
        }
    }
}

```
