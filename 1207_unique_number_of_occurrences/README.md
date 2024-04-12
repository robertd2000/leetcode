# [1207. Unique Number of Occurrences](https://leetcode.com/problems/find-words-containing-character/description/)

Given an array of integers `arr`, return `true` _if the number of occurrences of each value in the array is unique or `false` otherwise._

## Example 1:

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

## Example 2:

```
Input: arr = [1,2]
Output: false
```

## Example 3:

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

## Constraints:

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}

        for i in arr:
            hash[i] = hash.get(i, 0) + 1


        hashValues = len(hash.values())
        hashUnique = len(list(set(hash.values())))

        return hashValues == hashUnique

```
