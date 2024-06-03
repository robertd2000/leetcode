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
