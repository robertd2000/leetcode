# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the _maximum amount_ of water a container can store.

Notice that you may not slant the container.

## Example 1:

![example 1](image.png)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

## Example 2:

```
Input: height = [1,1]
Output: 1
```

## Constraints:

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

# Complexity

- **Time complexity:**
  `O(n)`
- **Space complexity:**
  `O(1)`

# Code

```python

from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height) - 1

        while l < r:
            lH, rH = height[l], height[r]

            square = min(lH, rH) * (r - l)

            if square > maximum:
                maximum = square
            if lH < rH:
                l+= 1
            else:
                r -= 1

        return maximum

```

```java

class Solution {
    public int maxArea(int[] height) {
        int max = 0;

        int l = 0;
        int r = height.length - 1;

        while (l < r) {
            int lH = height[l];
            int rH = height[r];

            int square = Math.min(lH, rH) * (r - l);

            if (square > max) {
                max = square;
            }

            if (lH < rH)
                l++;
            else
                r--;
        }

        return max;

    }
}

```

```cpp

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maximum = 0;

        int l = 0;
        int r = height.size() - 1;

        while (l < r) {
            int lHeight = height[l];
            int rHeight = height[r];

            int square = min(lHeight, rHeight) * (r - l);

            if (square > maximum) {
                maximum = square;
            }

            if (lHeight < rHeight) {
                l++;
            } else {
                r--;
            }
        }

        return maximum;
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

```cs

public class TwoSum {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.Length - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                return new int[] { l + 1, r + 1 };
            }

            if (numbers[l] + numbers[r] > target) {
                r--;
            }

            if (numbers[l] + numbers[r] < target) {
                l++;
            }
        }

        return new int[] {};
    }
}

```

```rs

impl TwoSum {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l = 0;
        let mut r = numbers.len() - 1;

        while l < r {
            if numbers[l] + numbers[r] == target {
                return vec![(l + 1) as i32, (r + 1) as i32];
            }

            if numbers[l] + numbers[r] > target {
                 r = r - 1;
            }

            if numbers[l] + numbers[r] < target {
                 l = l + 1;
            }
        }

         vec![0, 0]
    }
}

```
