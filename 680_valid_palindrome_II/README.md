# [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)

Given a string `s`, return `true` _if the `s` can be palindrome after deleting **at most one** character from it_.

## Example 1:

Input: s = "aba"
Output: true

## Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

## Example 1:

Input: s = "abc"
Output: false

## Constraints:

- `1 <= s.length <= 105`
- `s` consists of lowercase English letters.

```py

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1
            r -=1

        return True

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1

        return True

```

```ts
function validPalindrome(s: string): boolean {
  let l = 0;
  let r = s.length - 1;

  while (l < r) {
    if (s[l] !== s[r])
      return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
    l++;
    r--;
  }

  return true;
}

function isPalindrome(s: string, l: number, r: number): boolean {
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }

  return true;
}
```

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
  let l = 0;
  let r = s.length - 1;

  while (l < r) {
    if (s[l] != s[r])
      return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
    l++;
    r--;
  }

  return true;
};

function isPalindrome(s, l, r) {
  while (l < r) {
    if (s[l] != s[r]) return false;
    l++;
    r--;
  }

  return true;
}
```

```go

func validPalindrome(s string) bool {
	l, r := 0, len(s)-1

	for l < r {
		if s[l] != s[r] {
			return isPalindrome(s, l+1, r) || isPalindrome(s, l, r-1)
		}
		l++
		r--
	}

	return true
}

func isPalindrome(s string, l int, r int) bool {
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}

	return true
}

```
