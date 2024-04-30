# [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/description/?envType=daily-question&envId=2024-04-30)

A **wonderful** string is a string where _at most one_ letter appears an **odd** number of times.

- For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

Given a string word that consists of the first ten lowercase English letters (`'a'` through `'j'`), return _the **number of wonderful non-empty substrings** in word. If the same substring appears multiple times in word, then count **each occurrence** separately_.

A **substring** is a contiguous sequence of characters in a string.

## Example 1:

```
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
```

## Example 2:

```
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
```

## Example 3:

```
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
```

## Constraints:

- `1 <= word.length <= 10^5`
- `word` consists of lowercase English letters from `'a'` to `'j'`.

# Code

```python

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt, res, mask = [1] + [0] * 1023, 0, 0

        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            res += cnt[mask]
            for n in range(10):
                res += cnt[mask ^ 1 << n];
            cnt[mask] += 1

        return res

```
