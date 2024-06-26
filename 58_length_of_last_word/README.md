# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150)

Given a string `s` consisting of words and spaces, return the _length of the **last** word in the string._

A word is a maximal **substring** consisting of non-space characters onl

## Example 1:

```

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

```

## Example 2:

```

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

```

## Example 3:

```

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

```

## Constraints:

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

# Code

**Trim string and split**

```python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split(' ')
        return len(arr[-1])

```

**Iterate over string**

```python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, tail = 0, len(s) - 1

        while tail >= 0 and s[tail] == ' ':
            tail-=1
        while tail >= 0 and s[tail] != ' ':
            l += 1
            tail-=1

        return l

```
