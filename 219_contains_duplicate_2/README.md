# [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150)

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Example 1:

```

Input: nums = [1,2,3,1], k = 3
Output: true

```

## Example 2:

```

Input: nums = [1,0,1,1], k = 1
Output: true

```

## Example 3:

```

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```

## Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

# Code

```py

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for i, value in enumerate(nums):
            if value in hashMap and abs(hashMap[value] - i) <= k:
                return True
            hashMap[value] = i

        return False

```

```java

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int value = nums[i];
            if (hash.containsKey(value) && i - hash.get(value) <= k) {
                return true;
            }
            hash.put(value, i);
        }

        return false;
    }
}

```

```go

func containsNearbyDuplicate(nums []int, k int) bool {
    hashMap := map[int]int{}

    for i, val := range nums {
        hashVal, ok := hashMap[val]
        if ok && i - hashVal <= k {
            return true
        }
        hashMap[val] = i
    }

    return false
}

```
