[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

**Example 1:**

**Input:** n = 5, bad = 4
**Output:** 4
**Explanation:**
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

**Example 2:**

**Input:** n = 1, bad = 1
**Output:** 1

**Constraints:**

- `1 <= bad <= n <= 231 - 1`

[278. Первая плохая версия](https://leetcode.com/problems/first-bad-version/)

Вы менеджер по продукту и в настоящее время руководите командой по разработке нового продукта. К сожалению, последняя версия вашего продукта не проходит проверку качества. Поскольку каждая версия разрабатывается на основе предыдущей версии, все версии после плохой версии также плохие.

Предположим, у вас есть `n` версий `[1, 2, ..., n]` и вы хотите узнать первую плохую версию, которая делает все последующие плохими.

Вам дан API `bool isBadVersion(version)` который возвращает, является ли `version` плохой. Реализуйте функцию для поиска первой плохой версии. Вам следует минимизировать количество вызовов API.

**Пример 1:**

**Вход:** n = 5, плохо = 4
**Выход:** 4
**Объяснение:**
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Тогда 4 — первая плохая версия.

**Пример 2:**

**Вход:** n = 1, плохо = 1
**Выход:** 1

**Ограничения:**

- `1 <= плохо <= n <= 231 - 1`

Нужно решить задачу используя минимальное количество обращений к АПИ. Так как у нас версии идут от 1 до n то есть по возрастанию и все версии после плохой тоже плохие, то можно использовать бинарный поиск:

```typescript
let left = 1;
let right = n;
```

Выполняем цикл до тех пор, пока left меньше чем right. Находим срединное значение:

```typescript
let mid = Math.floor((left + right) / 2);
```

Если mid это плохая версия, то значит все что справа это тоже плохие версии, значит нужно искать слева, поэтому присваиваем right = mid. Так как мы ищем первую плохую версию, то присваиваем в right не mid + 1, а просто mid. Иначе, если mid это хорошая версия, все что слева это тоже хорошие версии и нужно искать справа.

Итоговый код:

```typescript
var solution = function (isBadVersion: any) {
  return function (n: number): number {
    let left = 1;
    let right = n;

    while (left < right) {
      let mid = Math.floor((left + right) / 2);

      if (isBadVersion(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return right;
  };
};
```

```python

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

```

```cpp

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1;
        int r = n;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (isBadVersion(m)) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return l;
    }
};

```

```java

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left <= right) {
            int middle = left + (right - left) / 2;

            if (isBadVersion(middle)) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        return left;
    }
}

```

```go

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    l, r := 1, n

    for l <= r {
        m := l + (r - l) / 2

        if isBadVersion(m) {
            r = m - 1
        } else {
            l = m + 1
        }
    }

    return l
}

```

```c

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int l = 1;
    int r = n;

    while (l <= r) {
        int m = l + (r - l) / 2;

        if (isBadVersion(m)) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }

    return l;
}

```

```cs

/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        int l = 0;
        int r = n;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (IsBadVersion(m)) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return l;
    }
}

```

```rs

// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
		let mut l = 1;
        let mut r = n;

        while l <= r {
            let mut m = l + (r - l) / 2;

            if self.isBadVersion(m) {
                r = m - 1
            } else {
                l = m + 1
            }
        }

        return l
    }
}

```

```kt

/* The isBadVersion API is defined in the parent class VersionControl.
      fun isBadVersion(version: Int) : Boolean {} */

class Solution: VersionControl() {
    override fun firstBadVersion(n: Int) : Int {
            var l: Long = 1
    var r: Long = n.toLong() + 1

    while (l < r) {
        val m = l + (r - l) / 2

        if (isBadVersion(m.toInt()))
            r = m
        else
            l = m + 1
    }

    return l.toInt()
	}
}

```

```js
/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let l = 1;
    let r = n;

    while (l <= r) {
      let m = l + Math.floor((r - l) / 2);
      if (isBadVersion(m)) {
        r = m - 1;
      } else {
        l = m + 1;
      }
    }

    return l;
  };
};
```
