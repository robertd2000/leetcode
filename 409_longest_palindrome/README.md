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

```ts
function longestPalindrome(s: string): number {
  const seen = new Set();

  let res = 0;

  for (let c of s) {
    if (seen.has(c)) {
      res += 2;
      seen.delete(c);
    } else {
      seen.add(c);
    }
  }

  if (seen.size) {
    res += 1;
  }

  return res;
}
```

```python

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()

        res = 0

        for i in s:
            if i in seen:
                seen.remove(i)
                res += 2
            else:
                seen.add(i)

        if seen:
            res += 1

        return res

```

```java

class Solution {
    public int longestPalindrome(String s) {
        int res = 0;
        int n = s.length();

        Set<Character> visited = new HashSet<>();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);

            if (visited.contains(c)) {
                res += 2;
                visited.remove(c);
            } else {
                visited.add(c);
            }
        }

        if (!visited.isEmpty()) res++;

        return res;
    }
}

```

```go

func longestPalindrome(s string) int {
	res := 0

	visited := make(map[rune]bool)

	for _, c := range s {
		if _, ok := visited[c]; ok {
			res += 2
			delete(visited, c)
		} else {
			visited[c] = true
		}
	}

	if len(visited) > 0 {
		res++
	}

	return res
}

```

```cpp

class Solution {
public:
    int longestPalindrome(string s) {
        int res = 0;

        set<char> visited;

        for (char c : s) {
            if (visited.find(c) != visited.end()) {
                res += 2;
                visited.erase(c);
            } else {
                visited.insert(c);
            }
        }

        if (!visited.empty()) res++;

        return res;
    }
};

```

```rs

use std::collections::HashSet;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut res = 0;

        let mut visited = HashSet::new();

        for c in s.chars() {
            if visited.contains(&c) {
                res += 2;
                visited.remove(&c);
            } else {
                visited.insert(c);
            }
        }

        if !visited.is_empty() {
            res += 1;
        }

        return res;
    }
}

```
