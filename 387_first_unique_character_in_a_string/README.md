# [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

Given a string `s`, _find the first non-repeating character in it and return its index_. If it does not exist, return `-1`.

## Example 1:

```

Input: s = "leetcode"
Output: 0

```

## Example 2:

```

Input: s = "loveleetcode"
Output: 2

```

## Example 3:

```

Input: s = "aabb"
Output: -1

```

## Constraints:

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Code

**Hash**

```ts
function firstUniqChar(s: string): number {
  const hash = {};

  for (let i of s) {
    if (i in hash) {
      hash[i] += 1;
    } else {
      hash[i] = 1;
    }
  }

  for (let i of s) {
    if (hash[i] == 1) {
      return s.indexOf(i);
    }
  }

  return -1;
}
```

```py

class Solution:
    def firstUniqChar(self, s: str) -> int:
        h_map = defaultdict(int)

        for i in s:
            h_map[i] += 1

        for i in range(len(s)):
            if h_map[s[i]] == 1:
                return i

        return -1

```

```java

class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (hashMap.get(c) == 1) return i;
        }

        return -1;
    }
}

```
