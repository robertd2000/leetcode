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

```py

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        min_len = min([len(i) for i in strs])

        for i in range(min_len):
            if self.is_common_prefix(strs, i + 1):
                res = strs[0][:i + 1]

        return res

    def is_common_prefix(self, strs: List[str], n: int) -> bool:
        prefix = strs[0][:n]

        for str in strs:
            if str[:n] != prefix:
                return False

        return True

```

```ts
function longestCommonPrefix(strs: string[]): string {
  strs.sort();

  let res = "";

  const first = strs.at(0) || "";
  const last = strs.at(-1) || "";

  const n = Math.min(first.length, last.length);

  for (let i = 0; i < n; i++) {
    if (first[i] != last[i]) return res;

    res += first[i];
  }

  return res;
}
```

```go

func longestCommonPrefix(strs []string) string {
    sort.Strings(strs)

    var res strings.Builder

    first, last := strs[0], strs[len(strs) - 1]

    n := min(len(first), len(last))

    for i := 0; i < n; i++ {
        if first[i] != last[i] {
            return res.String()
        }

        res.WriteByte(first[i])
    }

    return res.String()
}
```

```java

class Solution {
    public String longestCommonPrefix(String[] v) {
        StringBuilder ans = new StringBuilder();
        Arrays.sort(v);

        String first = v[0];
        String last = v[v.length - 1];

        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) != last.charAt(i)) {
                return ans.toString();
            }
            ans.append(first.charAt(i));
        }

        return ans.toString();
    }
}

```

```cpp

class Solution {
public:
    string longestCommonPrefix(vector<string>& v) {
        string ans = "";
        sort(v.begin(), v.end());
        int n = v.size();
        string first = v[0], last = v[n - 1];

        for (int i = 0; i < min(first.size(), last.size()); i++) {
            if (first[i] != last[i]) {
                return ans;
            }
            ans += first[i];
        }

        return ans;
    }
};

```
