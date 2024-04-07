# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/)

Given a string s containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if s is **valid**.

The following rules define a **valid** string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

## Example 1:

```
Input: s = "()"
Output: true
```

## Example 2:

```
Input: s = "(*)"
Output: true
```

## Example 3:

```
Input: s = "(*))"
Output: true
```

## Constraints:

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(1)`

# Code

```python

class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for ch in s:
            if ch == '(':
                cmax += 1
                cmin += 1
            if ch == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if ch == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

```
