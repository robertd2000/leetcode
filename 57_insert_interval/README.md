[57. Insert Interval](https://leetcode.com/problems/insert-interval/)

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` *after the insertion*.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

**Example 1:**

**Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Output:** [[1,5],[6,9]]

**Example 2:**

**Input:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Output:** [[1,2],[3,10],[12,16]]
**Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

**Constraints:**

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` is sorted by `starti` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 105`
  [57. Вставить интервал](https://leetcode.com/problems/insert-interval/)

Вам дан массив неперекрывающихся интервалов `intervals`, где `intervals[i] = [starti, endi]` представляют начало и конец `ith` интервала, а `intervals` отсортирован в порядке возрастания по `starti`. Вам также дан интервал `newInterval = [start, end]`, который представляет начало и конец другого интервала.

Вставьте `newInterval` в `intervals` таким образом, чтобы `intervals` по-прежнему был отсортирован в порядке возрастания по `starti`, а `intervals` по-прежнему не имел перекрывающихся интервалов (при необходимости объедините перекрывающиеся интервалы).

Верните `intervals` *после вставки*.

**Обратите внимание**, что вам не нужно изменять `intervals` на месте. Вы можете создать новый массив и вернуть его.

**Пример 1:**

**Вход:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Выход:** [[1,5],[6,9]]

**Пример 2:**

**Вход:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Выход:** [[1,2],[3,10],[12,16]]
**Объяснение:** Потому что новый интервал [4,8] перекрывается с [3,5],[6,7],[8,10].

**Ограничения:**

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` сортируется по `starti` в **возрастающем** порядке.
- `newInterval.length == 2`
- `0 <= start <= end <= 105`

Идея такая - нужно итерироваться по интервалам и на каждой итерации проверять, можно ли вставить новый интервал. Если новый интервал меньше текущего и не пересекается с ним, то нужно вставить его в результирующий массив res, а потом добавить все остальные интервалы, так как новый меньше их всех, так как массив с интервалами отсортирован:

```typescript
if (newInterval[1] < intervals[i][0]) {
  res.push(newInterval);
  return [...res, ...intervals.slice(i)];
}
```

Можно сравнить последний элемент нового интервала с первым элементом текущего и если он меньше, значит и первый элемент нового интервала меньше, тогда мы можем вставить его в res, а затем добавить все оставшиеся элементы массива newInterval и выйти из цикла. так как все оставльное уже вставлено и больше чем newInterval. Все что в res перед новым интервалом будет меньше него и не будет пересекаться с ним (см ниже)

Иначе проверим, что первый элемент нового интервала newInterval больше чем последний элемент текущего интервала. Тогда получится, что все элементы текущего интервала меньше чем нового newInterval и значит нужно вставить его в res перед новым интервалом и продолжить выполнения цикла:

```typescript
else if (newInterval[0] > intervals[i][1]) {
	res.push(intervals[i]);
}
```

Иначе получается, что newInterval пересекается с текущим интервалом и нужно обновить newInterval, чтобы знать их пересечение. Для этого надо найти начало и конец пересекающихся интервалов и обновить newInterval с их значениями:

```typescript
const start = Math.min(newInterval[0], intervals[i][0]);
const end = Math.max(newInterval[1], intervals[i][1]);
newInterval = [start, end];
```

После этого цикл продолжит выполняться, подставляя в res новые значения, если новый интервал newInterval больше чем текущий, возвращая результат, если найдено место, куда можно вставить newInterval (то есть когда он меньше текущего) или обновляя newInterval, когданайдено пересечение с текущим интервалом.

Если место куда нужно вставить newInterval так и не найдено, то нужно перед возвращением res после цикла добавить newInterval в res:

```typescript
res.push(newInterval);
```

Итоговый код:

```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const n = intervals.length;
  const res: number[][] = [];

  for (let i = 0; i < n; i++) {
    if (newInterval[1] < intervals[i][0]) {
      res.push(newInterval);
      return [...res, ...intervals.slice(i)];
    } else if (newInterval[0] > intervals[i][1]) {
      res.push(intervals[i]);
    } else {
      const start = Math.min(newInterval[0], intervals[i][0]);
      const end = Math.max(newInterval[1], intervals[i][1]);
      newInterval = [start, end];
    }
  }

  res.push(newInterval);

  return res;
}
```

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)

        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]

        res.append(newInterval)

        return res
```

```cpp

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        for (int i = 0; i < intervals.size(); i++) {
            vector<int> interval = intervals[i];

            if (newInterval[1] < interval[0]) {
                res.push_back(newInterval);
                res.insert(res.end(), intervals.begin() + i, intervals.end());
                return res;
            } else if (newInterval[0] > interval[1]) {
                res.push_back(interval);
            } else {
                int start = min(newInterval[0], interval[0]);
                int end = max(newInterval[1], interval[1]);
                newInterval = {start, end};
            }
        }

        res.push_back(newInterval);

        return res;
    }
};

```

```java

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) {
                result.add(interval);
            } else if (interval[0] > newInterval[1]) {
                result.add(newInterval);
                newInterval = interval;
            } else {
                int start = Math.min(interval[0], newInterval[0]);
                int end = Math.max(interval[1], newInterval[1]);
                newInterval = new int[] {start, end};
            }
        }

        result.add(newInterval);

        return result.toArray(new int[result.size()][]);
    }
}

```

```go

func insert(intervals [][]int, newInterval []int) [][]int {
    var res [][]int

    for idx, interval := range intervals {
        if interval[0] > newInterval[1] {
            res = append(res, newInterval)
            res = append(res, intervals[idx:]...)
            return res
        } else if interval[1] < newInterval[0] {
            res = append(res, interval)
        } else {
            start := min(interval[0], newInterval[0])
            end := max(interval[1], newInterval[1])
            newInterval = []int {start, end}
        }
    }

    res = append(res, newInterval)

    return res
}

func max(a int, b int) int {
    if a > b {
        return a
    }

    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }

    return b
}

```

```c

int **insert(int **intervals, int intervalsSize, int *intervalsColSize, int *newInterval, int newIntervalSize, int *returnSize, int **returnColumnSizes) {
    int **result = (int **)malloc((intervalsSize + 1) * sizeof(int *));
    *returnSize = 0;
    *returnColumnSizes = (int *)malloc((intervalsSize + 1) * sizeof(int));

    int i = 0;
    while (i < intervalsSize && intervals[i][1] < newInterval[0]) {
        result[*returnSize] = (int *)malloc(2 * sizeof(int));
        result[*returnSize][0] = intervals[i][0];
        result[*returnSize][1] = intervals[i][1];
        (*returnColumnSizes)[*returnSize] = 2;
        (*returnSize)++;
        i++;
    }

    while (i < intervalsSize && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = (newInterval[0] < intervals[i][0]) ? newInterval[0] : intervals[i][0];
        newInterval[1] = (newInterval[1] > intervals[i][1]) ? newInterval[1] : intervals[i][1];
        i++;
    }

    result[*returnSize] = (int *)malloc(2 * sizeof(int));
    result[*returnSize][0] = newInterval[0];
    result[*returnSize][1] = newInterval[1];
    (*returnColumnSizes)[*returnSize] = 2;
    (*returnSize)++;

    while (i < intervalsSize) {
        result[*returnSize] = (int *)malloc(2 * sizeof(int));
        result[*returnSize][0] = intervals[i][0];
        result[*returnSize][1] = intervals[i][1];
        (*returnColumnSizes)[*returnSize] = 2;
        (*returnSize)++;
        i++;
    }

    return result;
}

```
