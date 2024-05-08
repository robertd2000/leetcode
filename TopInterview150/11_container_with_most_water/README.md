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

```go

package maxarea

func maxArea(height []int) int {
	max := 0

	l, r := 0, len(height)-1

	for l < r {
		lHeight, rHeight := height[l], height[r]
		square := min(lHeight, rHeight) * (r - l)

		if square > max {
			max = square
		}

		if lHeight < rHeight {
			l++
		} else {
			r--
		}
	}

	return max
}

func min(first, second int) int {
	if first < second {
		return first
	}

	return second
}


```

```ts
function maxArea(height: number[]): number {
  let l = 0;
  let r = height.length - 1;
  let max = 0;

  while (l < r) {
    const lH = height[l];
    const rH = height[r];
    let square = Math.min(lH, rH) * (r - l);

    if (square > max) {
      max = square;
    }

    if (lH < rH) {
      l += 1;
    } else {
      r -= 1;
    }
  }

  return max;
}
```

```rs

use std::cmp::Ordering;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        Self::max_area_acc(&height, 0, 0)
    }

    pub fn max_area_acc(heights: &[i32], acc: i32, max_height: i32) -> i32 {
        let len = heights.len();
        if heights.len() < 2 {
            return acc;
        }

        let mut i = 0;
        let mut j = len - 1;

        let first = loop {
            if i >= j {
                break max_height;
            }

            let first = heights[i];
            if first > max_height {
                break first;
            }

            i += 1;
        };

        let last = loop {
            if i >= j {
                break max_height;
            }

            let last = heights[j];
            if last > max_height {
                break last;
            }

            j -= 1;
        };

        let height = first.min(last);
        let width = (j - i) as i32;
        if width == 0 {
            return acc;
        }

        match first.cmp(&last) {
            Ordering::Less => {
                let height = first;
                let area = width * height;
                Self::max_area_acc(&heights[(i + 1)..(j + 1)], acc.max(area), height) // leave right
            },
            Ordering::Equal => {
                let height = first;
                let area = width * height;
                Self::max_area_acc(&heights[(i + 1)..j], acc.max(area), height) // dont leave anything
            },
            Ordering::Greater => {
                let height = last;
                let area = width * height;
                Self::max_area_acc(&heights[i..j], acc.max(area), height) // leave left
            },
        }
    }
}

```
