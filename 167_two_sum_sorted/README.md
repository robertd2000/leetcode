# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Given a **1-indexed** array of integers numbers that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the _indices of the two numbers_, `index1` and `index2`, _added by one as an integer array `[index1, index2]` of length 2_.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Example 1:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

## Example 2:

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

## Example 3:

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

## Constraints:

```
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
```

_Only one valid answer exists._

# Complexity

- **Time complexity:**
  `O(n)`
- **Space complexity:**
  `O(1)`

```python

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r = r - 1
            if numbers[l] + numbers[r] < target:
                l = l + 1
        return []

```

```java

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                return new int[] { left + 1, right + 1 };
            } else if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[] { left, right };
    }
}

```

```cpp

class TwoSum {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                return {l + 1, r + 1};
            }
            if (numbers[l] + numbers[r] > target) {
                r--;
            }
             if (numbers[l] + numbers[r] < target) {
                l++;
            }
        }

       return {l + 1, r + 1};
    }
};

```

```c

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));

    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int l = 0;
    int r = numbersSize - 1;

    while (l < r) {
        if (numbers[l] + numbers[r] == target) {
            result[0] = l + 1;
            result[1] = r + 1;

            *returnSize = 2;
            return result;
        }

        if (numbers[l] + numbers[r] > target) {
            r--;
        }

        if (numbers[l] + numbers[r] < target) {
            l++;
        }
    }
    *returnSize = 0;
    free(result);
    return NULL;
}

```

```go

package twosumsorted

func twoSum(numbers []int, target int) []int {
	l, r := 0, len(numbers)-1

	for l < r {
		if numbers[l]+numbers[r] == target {
			return []int{l + 1, r + 1}
		}
		if numbers[l]+numbers[r] > target {
			r = r - 1
		}
		if numbers[l]+numbers[r] < target {
			l = l + 1
		}
	}

	return []int{l, r}
}

```

```ts
function twoSum(numbers: number[], target: number): number[] {
  let [l, r] = [0, numbers.length - 1];

  while (l < r) {
    if (numbers[l] + numbers[r] == target) {
      return [l + 1, r + 1];
    } else if (numbers[l] + numbers[r] > target) {
      r--;
    } else if (numbers[l] + numbers[r] < target) {
      l++;
    }
  }
  return [];
}
```
