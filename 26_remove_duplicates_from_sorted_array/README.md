# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return _the number of unique elements in_ `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Custom Judge:**

The judge will test your solution with the following code:

```

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

## Example 1:

```

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

## Example 2:

```

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

## Constraints:

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

Используем 2 указателя - `i` на текущий элемент и `k` на позицию уникального. Начинаем цикл с 1, т.к. первый элемент уникален.Если текущий элемент `nums[i]` не равен последнему уникальному `nums[k]`, то значит он уникален и мы инкрементируем указатель `k` на уникальнвй элемент, затем присваиваем в эту позицию текущий элемент:

```
nums[k] = nums[i]
```

# Code

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let k = 0;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] != nums[k]) {
      k++;
      nums[k] = nums[i];
    }
  }

  return k + 1;
};
```

```python

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]

        return idx + 1

```

```java

class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[index] = nums[i];
                index++;
            }
        }

        return index;
    }
}

```

```go

func removeDuplicates(nums []int) int {
    idx := 0

    for _, val := range nums {
        if val != nums[idx] {
            idx++
            nums[idx] = val
        }
    }

    return idx + 1
}

```

```ts
function removeDuplicates(nums: number[]): number {
  const count = new Array<number>(201).fill(0);

  for (let num of nums) {
    count[num + 100]++;
  }

  let pos = 0;

  for (let i = 0; i < count.length; i++) {
    if (count[i]) {
      nums[pos] = i - 100;
      pos++;
    }
  }

  return pos;
}
```
