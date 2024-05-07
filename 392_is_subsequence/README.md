# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150)

Given two strings `s` and `t`, return `true` _if `s` is a **subsequence** of `t`, or `false` otherwise._

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Example 1:

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

## Example 2:

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Constraints:

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(1)`

# Code

```python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return False
        if n == 0:
            return True

        j = 0

        for i in range(m):
            if j < n and s[j] == t[i]:
                j += 1

        return j == n

```

```java

class Solution {
    public boolean isSubsequence(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n > m) {
            return false;
        }

        if (n == 0) {
            return true;
        }

        int j = 0;

        for (int i = 0; i < m; i++) {
            if (j < n && s.charAt(j) == t.charAt(i)) {
                j++;
            }
        }

        return j == n;
    }
}

```
