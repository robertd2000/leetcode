[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

**Example 2:**

**Input:** root = [1]
**Output:** [[1]]

**Example 3:**

**Input:** root = []
**Output:** []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

[102. Обход порядка уровней двоичного дерева](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Для заданного `корня` двоичного дерева вернуть _обход порядка уровней значений его узлов_. (т. е. слева направо, уровень за уровнем).

**Пример 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**Вход:** root = [3,9,20,null,null,15,7]
**Выход:** [[3],[9,20],[15,7]]

**Пример 2:**

**Вход:** root = [1]
**Выход:** [[1]]

**Пример 3:**

**Вход:** root = []
**Выход:** []

**Ограничения:**

- Количество узлов в дереве находится в диапазоне `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

Решение с помощью очередей. Будем использовать 2 очереди - queue как хранилище узлов дерева, levels как хранилище уровней. По умолчанию в queue будет помещен root, а levels будет пустым. До тех пор, пока в queue есть элементы, выполняем цикл, в котором извлекаем узел current из начала queue (так как нужно сохранить порядок) и заполняем levels дочерними элементами текущего current:

```typescript
const current = queue.shift();

if (current.left) {
  levels.push(current.left);
}

if (current.right) {
  levels.push(current.right);
}
```

Далее, если очередь queue пустая на данной итерации (после извлечения первого элемента), то заполнит результат элементами текущего уровня дерева из levels, после чего перезапишем элементы levels в queue, а levels присвоим пустой массив (очистим текущий уровень):

```typescript
if (!queue.length) {
  if (levels.length) {
    result.push(levels.map((n) => n.val));
  }
  queue = levels;
  levels = [];
}
```

```typescript
function levelOrder(root: TreeNode | null): number[][] {
  if (root === null) return [];

  let queue = [root];
  let levels = [];
  const result: number[][] = [[root.val]];

  while (queue.length) {
    const current = queue.shift();

    if (current.left) {
      levels.push(current.left);
    }

    if (current.right) {
      levels.push(current.right);
    }

    if (!queue.length) {
      if (levels.length) {
        result.push(levels.map((n) => n.val));
      }
      queue = levels;
      levels = [];
    }
  }

  return result;
}
```

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return

        res = [[root.val]]

        q = [root]
        t = []

        while len(q) > 0:
            cur = q.pop(0)

            if cur.left is not None:
                t.append(cur.left)
            if cur.right is not None:
                t.append(cur.right)
            if not q:
                if t:
                    res.append([n.val for n in t])
                q = t
                t = []

        return res
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        bfs(root, 0, res);
        return res;
    }

    private void bfs(TreeNode root, int level, List<List<Integer>> res) {
        if (root == null) return;
        if (res.size() <= level) res.add(new ArrayList<>());

        res.get(level).add(root.val);
        bfs(root.left, level + 1, res);
        bfs(root.right, level + 1, res);
    }
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> res = new LinkedList<List<Integer>>();

        if(root == null) return res;

        queue.offer(root);

        while(!queue.isEmpty()){
            int levelNum = queue.size();
            List<Integer> subList = new LinkedList<Integer>();
            for(int i=0; i<levelNum; i++) {
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                subList.add(queue.poll().val);
            }
            res.add(subList);
        }

        return res;
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        bfs(root, 0, res);
        return res;
    }

private:
    void bfs(TreeNode* root, int level, vector<vector<int>>& res) {
        if (root == 0) return;

        if (res.size() <= level) {
            res.push_back({});
        }
        res[level].push_back(root->val);
        bfs(root->left, level + 1, res);
        bfs(root->right, level + 1, res);
    }
};

```

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const res = [];

  dfs(root, 0, res);
  return res;
};

function dfs(root, level, res) {
  if (root) {
    if (res.length <= level) {
      res.push([]);
    }

    res[level].push(root.val);
    dfs(root.left, level + 1, res);
    dfs(root.right, level + 1, res);
  }

  return;
}
```
