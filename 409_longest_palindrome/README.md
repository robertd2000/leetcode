# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04)

Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, `"Aa"` is not considered a palindrome.

## Example 1:

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

## Example 2:

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
```

## Constraints:

- `1 <= s.length <= 2000`
- `s` consists of lowercase and/or uppercase English letters only.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```ts
function longestPalindrome(s: string): number {
  const map = {};
  let res = 0;

  for (let i of s) {
    if (i in map) {
      delete map[i];
      res++;
    } else {
      map[i] = 1;
    }
  }

  if (!isEmpty(map)) {
    return res * 2 + 1;
  }

  return res * 2;
}

function isEmpty(obj) {
  for (const prop in obj) {
    if (Object.hasOwn(obj, prop)) {
      return false;
    }
  }

  return true;
}
```
