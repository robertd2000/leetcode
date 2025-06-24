[350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

**Example 1:**

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

**Example 2:**

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

**Follow up:**

- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

#### Solutions

##### **hash table approach**

Using HashMap to store occurrences of elements in the `nums1` array.
Iterate `x` in `nums2` array, check if `cnt[x] > 0` then append `x` to our answer and decrease `cnt[x]` by one.
To optimize the space, we ensure `len(nums1) <= len(nums2)` by swapping `nums1` with `nums2` if `len(nums1) > len(nums2)`.

Используем хэш таблицу - сначала подсчитаем количество повторений в `nums1`, после чего пройдемся по `nums2` и проверим, есть ли он в `nums1` и что он там все еще есть - `cnt[x] > 0`. Если да, то добавим его в результат и уменьшим количество его повторений в хэш таблице на 1.

Для оптимизации пространства мы можем менять местами `nums1` и `nums2` если `len(nums1) > len(nums2)`

**Complexity:**

Time: O(M + N), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
Space: O(min(M, N))

```py

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
          return self.intersect(nums2, nums1)

        res = []

        h = defaultdict(int)

        for i in nums1:
            h[i] += 1

        for i in nums2:
            if i in h and h[i] > 0:
                res.append(i)
                h[i] -= 1

        return res

```

**sorted**

**Complexity:**

Time: `O(MlogM + NlogN)`, where `M <= 1000` is length of `nums1` array, `N <= 1000` is length of `nums2` array.
Extra Space (without counting output as space): `O(sorting)`

Отсортируем оба массива и используем два указателя: если они ссылаются на равные элементы, то добавляем их в результат и инкрементим указатели. Если `a[i] < b[j]`, то значит что нам нужно увеличить `i` на 1, т.к. он слишком мал, а нам нужно получить элемент равный `b[j]`. Иначе увеличим `j`

```py

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = sorted(nums1)
        b = sorted(nums2)
        res = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1

            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return res

```
