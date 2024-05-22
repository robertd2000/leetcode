# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/?envType=daily-question&envId=2024-05-22)

Given a string `s`, partition `s` such that every **substring** of the partition is a
**palindrome**. Return _all possible palindrome partitioning of `s`._

## Example 1:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

## Example 2:

```
Input: s = "a"
Output: [["a"]]
```

## Constraints:

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

# Code

```python

class Solution(object):
    @cache
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        return ans

```
