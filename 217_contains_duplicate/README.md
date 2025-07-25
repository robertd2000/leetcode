[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

**Input:** nums = [1,2,3,1]
**Output:** true

**Example 2:**

**Input:** nums = [1,2,3,4]
**Output:** false

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]
**Output:** true

**Constraints:**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

[217. Содержит дубликаты](https://leetcode.com/problems/contains-duplicate/)

Для заданного целочисленного массива `nums` верните `true`, если какое-либо значение встречается **как минимум дважды** в массиве, и верните `false`, если каждый элемент отличается.

**Пример 1:**

**Вход:** nums = [1,2,3,1]
**Выход:** true

**Пример 2:**

**Вход:** nums = [1,2,3,4]
**Выход:** false

**Пример 3:**

**Вход:** nums = [1,1,1,3,3,4,3,2,4,2]
**Выход:** true

**Ограничения:**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

Есть 3 способа решить эту задачу:

- с помощью сортировки
- с помощью хэш таблицы
- с помощью хэш сета

1 Способ - сортировка. Отсортируем массив и проитерируемся по нему. На каждой итерации сравним текущий элемент с предыдущим и если они равны, то значит есть дубликаты и тогда вернем `true`. Иначе, после цикла, вернем `false`, так как не встретили дубликатов:

```typescript
function containsDuplicate(nums: number[]): boolean {
  nums.sort();

  const n = nums.length;

  for (let i = 0; i < n - 1; i++) {
    if (nums[i] === nums[i + 1]) {
      return true;
    }
  }

  return false;
}
```

Сложность алгоритма:

- по времени - `O(n log n)` - из-за сортировки
- по памяти - `O(1)`

2 Способ - хэш таблица. Записываем сколько раз встречаются элементы в хэш таблицу и если встретилось значение больше `1`, то значит есть дубликат:

```typescript
function containsDuplicate(nums: number[]): boolean {
  const map = {};

  for (let num of nums) {
    map[num] = map[num] ? map[num] + 1 : 1;

    if (map[num] > 1) return true;
  }

  return false;
}
```

3 Способ - хэш сет. Самый легкий способ проверить массив на дубликаты - это создать сет и сравнить их длину. Если есть дубликаты, то длина сета будет меньше длины массива, так как сет может содержать лишь уникальные значения:

```typescript
function containsDuplicate(nums: number[]): boolean {
  const set = new Set(nums);

  return nums.length !== set.size;
}
```

```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const set = new Set();

  for (let num of nums) {
    if (set.has(num)) return true;
    set.add(num);
  }

  return false;
};
```

```python
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)

        for i in nums:
            map[i] += 1
            if map[i] > 1:
                return True

        return False
```

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        nums.sort()

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
```

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return len(s) != len(nums)
```

```python

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False

```

```java

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<Integer>();

        for (int num : nums) {
            if (hashSet.contains(num)) {
                return true;
            }

            hashSet.add(num);
        }
        return false;
    }
}

```

```go

func containsDuplicate(nums []int) bool {
    count := make(map[int]int)

    for _, i := range nums {
        if _, ok := count[i]; ok {
            return true
        }

        count[i] = 1
    }

    return false
}

```

```cpp

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> counter;

        for (int num : nums) {
            if (counter.find(num) != counter.end()) return true;
            counter[num] = true;
        }

        return false;
    }
};

```

```rs

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()

        for num in nums:
            if num in count:
                return True
            count.add(num)

        return False

```
