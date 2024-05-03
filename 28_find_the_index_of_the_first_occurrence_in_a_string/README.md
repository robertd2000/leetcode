# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Example 1:

```

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

```

## Example 2:

```

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

```

## Constraints:

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

# Code

```python

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        l, r = 0, m - 1

        if m > n:
            return -1

        while l < n:
            if l < n and haystack[l] == needle[0]:
                k = 0
                for i in range(0, m):
                    if i + l < n and haystack[i + l] == needle[i]:
                        k += 1
                if k == m:
                    return l
                l += 1
            else:
                l += 1

        return -1

```
