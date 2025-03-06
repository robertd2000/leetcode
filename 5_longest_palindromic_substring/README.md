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

```ts
function longestPalindrome(s: string): string {
  const n = s.length;

  let maxLen = 0;
  let res = "";

  for (let i = 0; i < n; i++) {
    let l = i;
    let r = i;

    while (l >= 0 && r < n && s[l] === s[r]) {
      let diff = r - l + 1;
      if (diff > maxLen) {
        maxLen = diff;
        res = s.slice(l, r + 1);
      }
      l -= 1;
      r += 1;
    }
    l = i;
    r = i + 1;

    while (l >= 0 && r < n && s[l] === s[r]) {
      let diff = r - l + 1;
      if (diff > maxLen) {
        maxLen = diff;
        res = s.slice(l, r + 1);
      }
      l -= 1;
      r += 1;
    }
  }

  return res;
}
```

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

```go

func longestPalindrome(s string) string {
    res := ""
    maxLen := 0

    for i := 0; i < len(s); i++ {
        l, r := i, i

        for l >= 0 && r < len(s) && s[l] == s[r] {
            if r - l + 1 > maxLen {
                res = s[l: r + 1]
                maxLen = r - l + 1
            }

            l--
            r++
        }

        l, r = i, i + 1

        for l >= 0 && r < len(s) && s[l] == s[r] {
            if r - l + 1 > maxLen {
                res = s[l: r + 1]
                maxLen = r - l + 1
            }

            l--
            r++
        }
    }

    return res
}

```

```java

class Solution {
    public String longestPalindrome(String s) {
        String result = "";

        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i;

            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 > maxLength) {
                    result = s.substring(left, right + 1);
                    maxLength = right - left + 1;
                }
                left--;
                right++;
            }

            left = i;
            right = i + 1;

            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 > maxLength) {
                    result = s.substring(left, right + 1);
                    maxLength = right - left + 1;
                }
                left--;
                right++;
            }
        }

        return result;
    }
}

```

```cpp

class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";
        int maxLen = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int l = i;
            int r = i;

            while (l >= 0 && r < n && s[l] == s[r]) {
                int diff = r - l + 1;
                if (diff > maxLen) {
                    maxLen = diff;
                    res = s.substr(l, diff);
                }
                l--;
                r++;
            }

            l = i;
            r = i + 1;

            while (l >= 0 && r < n && s[l] == s[r]) {
                int diff = r - l + 1;
                if (diff > maxLen) {
                    maxLen = diff;
                    res = s.substr(l, diff);
                }
                l--;
                r++;
            }
        }

        return res;
    }
};

```

```c

char* longestPalindrome(char* s) {
    int maxLen = 0;
    int n = strlen(s);

    char* res;

    for (int i = 0; i < n; i++) {
        int l = i;
        int r = i;

        while (l >= 0 && r < n && s[l] == s[r]) {
            int diff = r - l + 1;
            if (diff > maxLen) {
                maxLen = diff;
                res = malloc(maxLen + 1);
                memcpy(res, &s[l], maxLen);
                res[maxLen] = '\0';
            }
            l--;
            r++;
        }

        l = i;
        r = i + 1;

        while (l >= 0 && r < n && s[l] == s[r]) {
            int diff = r - l + 1;
            if (diff > maxLen) {
                maxLen = diff;
                res = malloc(maxLen + 1);
                memcpy(res, &s[l], maxLen);
                res[maxLen] = '\0';
            }
            l--;
            r++;
        }
    }

    return res;
}

```

```py

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        freqS = [0] * 26
        freqP = [0] * 26

        n = len(s)
        m = len(p)

        if n < m:
            return res

        for i in range(m):
            freqS[ord(s[i]) - ord('a')] += 1
            freqP[ord(p[i]) - ord('a')] += 1

        start = 0
        end = m

        if freqS == freqP:
            res.append(start)

        while end < n:
            freqS[ord(s[start]) - ord('a')] -= 1
            freqS[ord(s[end]) - ord('a')] += 1

            if freqS == freqP:
                res.append(start + 1)
            start += 1
            end += 1

        return res

```
