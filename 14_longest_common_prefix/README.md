# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Example 1:

```

Input: strs = ["flower","flow","flight"]
Output: "fl"

```

## Example 2:

```

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

## Constraints:

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

# Code

```py

from typing import List


class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)

        first = v[0]
        last = v[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans

```
