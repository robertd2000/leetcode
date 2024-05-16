# [290. Word Pattern](https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150)

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

## Example 1:

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

```

## Example 2:

```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

## Example 3:

```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

## Constraints:

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` **does not contain** any leading or trailing spaces.
- All the words in `s` are separated by a **single space.**

```python

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h1 = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        for i in range(len(s)):
            if s[i] not in h1:
                h1[s[i]] = pattern[i]
            elif h1[s[i]] != pattern[i]:
                return False

        return True

```
