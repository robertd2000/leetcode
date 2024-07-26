# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/?envType=daily-question&envId=2024-04-12)

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Example 1:

![example 1](<![example](image.png)>)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

## Example 2:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints:

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 10^5`

```python

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 1, len(height) - 1

        lmax = height[0]
        rmax = height[-1]

        while l <= r:

            lmax = max([height[l], lmax])
            rmax = max([height[r], rmax])

            if rmax >= lmax:
                res += lmax - height[l]
                l += 1
            else:
                res += rmax - height[r]
                r-= 1

        return res

```

```java

class Solution {
    public int trap(int[] height) {
        int result = 0;

        int n = height.length;
        int left = 0;
        int right = n - 1;

        int leftMax = height[0];
        int rightMax = height[n - 1];

        while (left <= right) {
            leftMax = Math.max(height[left], leftMax);
            rightMax = Math.max(height[right], rightMax);

            if (rightMax >= leftMax) {
                result += leftMax - height[left];
                left++;
            } else {
                result += rightMax - height[right];
                right--;
            }
        }

        return result;
    }
}

```

```go

func trap(height []int) int {
    res, n := 0, len(height) - 1
    l, r, lMax, rMax := 0, n, 0, height[n]

    for l <= r {
        lMax = max(height[l], lMax)
        rMax = max(height[r], rMax)

        if rMax >= lMax {
            res += lMax - height[l]
            l++
        } else {
            res += rMax - height[r]
            r--
        }
    }

    return res
}

func max(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

```

```c

int trap(int* height, int heightSize) {
    int left = 1;
    int right = heightSize - 2;

    int leftMax = height[0];
    int rightMax = height[heightSize - 1];

    int result = 0;

    while (left <= right) {
        if (leftMax < rightMax) {
            if (height[left] > leftMax) {
                leftMax = height[left];
            }
            result += leftMax - height[left];
            left++;
        } else {
            if (height[right] > rightMax) {
                rightMax = height[right];
            }
            result += rightMax - height[right];
            right--;
        }
    }

    return result;
}

```
