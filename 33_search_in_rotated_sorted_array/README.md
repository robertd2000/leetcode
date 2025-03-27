# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/trapping-rain-water/description/?envType=daily-question&envId=2024-04-12)

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` `(1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or `-1` if it is not in nums.

You must write an algorithm with `O(log n)` runtime complexity.

## Example 1:

```

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

```

## Example 2:

```

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

## Example 3:

```

Input: nums = [1], target = 0
Output: -1

```

## Constraints:

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of nums are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

```ts
function search(nums: number[], target: number): number {
  const n = nums.length;
  let l = 0;
  let r = n - 1;

  while (l <= r) {
    let mid = Math.floor((l + r) / 2);

    if (nums[mid] == target) return mid;

    if (nums[l] <= nums[mid]) {
      if (nums[l] <= target && target <= nums[mid]) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    } else {
      if (nums[mid] <= target && target <= nums[r]) {
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
  }

  return -1;
}
```

```py

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

```

```java

class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int l = 0;
        int r = n - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) return m;

            if (nums[l] <= nums[m]) {
                if (nums[m] >= target && nums[l] <= target) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if (nums[m] <= target && target <= nums[r]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
}

```

```cpp

  class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();

        int l = 0;
        int r = n - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) return m;

            if (nums[l] <= nums[m]) {
                if (nums[m] >= target && nums[l] <= target) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if (nums[m] <= target && target <= nums[r]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
};

```
