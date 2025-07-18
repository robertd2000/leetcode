[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

**Example 2:**

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

**Constraints:**

- `1 <= n <= 45`

[70. Подъем по лестнице](https://leetcode.com/problems/climbing-stairs/)

Вы поднимаетесь по лестнице. Чтобы достичь вершины, нужно сделать `n` шагов.

Каждый раз вы можете подняться на `1` или `2` шага. Сколькими различными способами вы можете подняться на вершину?

**Пример 1:**

**Ввод:** n = 2
**Вывод:** 2
**Объяснение:** Есть два способа подняться на вершину.

1. 1 шаг + 1 шаг
2. 2 шага

**Пример 2:**

**Ввод:** n = 3
**Вывод:** 3
**Объяснение:** Есть три способа подняться на вершину.

1. 1 шаг + 1 шаг + 1 шаг
2. 1 шаг + 2 шага
3. 2 шага + 1 шаг

**Ограничения:**

- `1 <= n <= 45`

Это задачи динамического программирования. Суть в том чтобы использовать результаты предыдущих вычислений. Нужно начать с конца - чтобы достичь последней "ступеньки" нужно - с последней ступеньки один способ, с предпоследней - тоже один. Далее знаю результат последних 2 ступенек мы можем рассчитать сколько способов для каждой ступеньки - предыдущая + текущая:

```typescript
function climbStairs(n: number): number {
  if (n < 2) return 1;

  let prev = 1;
  let curr = 1;

  for (let i = 2; i <= n; i++) {
    let temp = curr;
    curr = prev + curr;
    prev = temp;
  }

  return curr;
}
```

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        if n < 2:
            return 1

        prev = 1
        curr = 1

        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr
```

```java

class Solution {
    public int climbStairs(int n) {
        if (n < 2)
            return 1;

        int curr = 1;
        int prev = 1;

        for (int i = 2; i <= n; i++) {
            int temp = curr;
            curr = prev + curr;
            prev = temp;
        }

        return curr;
    }
}

```
