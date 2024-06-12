# [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions)

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Example 1:

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

## Example 2:

```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints:

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

**Counting sort**:

```py

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 4

        for i in nums:
            count[i] += 1

        pos = 0

        for i in range(len(count)):
            for j in range(count[i]):
                nums[pos] = i
                pos += 1

        return nums

```

```java

class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[4];

        for (int num : nums) {
            count[num]++;
        }

        int pos = 0;

        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0) {
                nums[pos] = i;
                count[i]--;
                pos++;
            }
        }
    }
}

```

**Pointers**

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

```
