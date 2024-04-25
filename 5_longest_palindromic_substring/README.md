# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions)

Given a string `s`, return _the longest palindromic substring in `s`._

**A string is palindromic if it reads the same forward and backward.**

## Example 1:

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

## Example 2:

```
Input: s = "cbbd"
Output: "bb"
```

## Constraints:

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

# Code

```python

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxLen = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

        return res

```
