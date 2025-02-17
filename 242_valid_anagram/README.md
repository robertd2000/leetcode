# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150)

Given two strings `s` and `t`, return `true` _if `t` is an anagram of `s`, and `false` otherwise._

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Example 1:

```
Input: s = "anagram", t = "nagaram"
Output: true
```

## Example 2:

```
Input: s = "rat", t = "car"
Output: false
```

## Constraints:

- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

**Follow-up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Code

**Hash table**

```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False

        h1 = {}
        h2 = {}

        for i in range(n):
            c1 = h1.get(s[i], 0)
            c2 = h2.get(t[i], 0)

            h1[s[i]] = c1 + 1
            h2[t[i]] = c2 + 1

        return h1 == h2

```

```ts
function isAnagram(s: string, t: string): boolean {
  return s.split("").sort().join("") === t.split("").sort().join("");
}
```

```java

class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        }

        Map<Character, Integer> hash = new HashMap<>();

        for (char c : s.toCharArray()) {
            hash.put(c, hash.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            hash.put(c, hash.getOrDefault(c, 0) - 1);
            if (hash.getOrDefault(c, 0) < 0) {
                return false;
            }

        }

        return true;
    }
}

```

```go

func isAnagram(s string, t string) bool {
	n, m := len(s), len(t)

	if n != m {
		return false
	}

	hash := map[rune]int{}

	for _, c := range s {
		val := hash[c]
		hash[c] = val + 1
	}

	for _, c := range t {
		val := hash[c]
		hash[c] = val - 1

		if hash[c] < 0 {
			return false
		}
	}

	return true
}

```

**Hash array**

```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        BOUND = 97
        n = len(s)
        m = len(t)

        if n != m:
            return False

        counter = [0] * 26

        for i in s:
            counter[ord(i) - BOUND] += 1

        for i in t:
            counter[ord(i) - BOUND] -= 1
            if counter[ord(i) - BOUND] < 0:
                return False

        return True

```

```ts
function isAnagram(s: string, t: string): boolean {
  const n = s.length;
  const m = t.length;

  if (n !== m) return false;

  const hash = new Map<string, number>();

  for (const i of s) {
    const value = hash.get(i) || 0;
    hash.set(i, value + 1);
  }

  for (const i of t) {
    const value = hash.get(i) || 0;
    hash.set(i, value - 1);

    if (hash.has(i) && hash.get(i) < 0) {
      return false;
    }
  }

  return true;
}
```

```java

class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        }

        int[] counter = new int[26];

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            counter[c - 'a']++;
        }

        for (int i = 0; i < m; i++) {
            char c = t.charAt(i);
            counter[c - 'a']--;

            if (counter[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}

```

```go

func isAnagram(s string, t string) bool {
	n, m := len(s), len(t)
	BOUND := 97

	if n != m {
		return false
	}

	count := [26]int{}

	for _, c := range s {
		count[int(c)-BOUND]++
	}

	for _, c := range t {
		count[int(c)-BOUND]--

		if count[int(c)-BOUND] < 0 {
			return false
		}
	}

	return true
}

```

**Sorting**

```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

```

```java

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}

```

```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        for i in s:
            val = hashMap.get(i, 0) + 1
            hashMap[i] = val

        for i in t:
            val = hashMap.get(i, 0) - 1
            hashMap[i] = val

            if val < 0:
                return False

        for i in hashMap.values():
            if i > 0:
                return False

        return True

```

```cpp

class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.length();
        int m = t.length();

        if (n != m) return false;

        unordered_map<char, int> hash;

        for (char ch: s) {
            hash[ch]++;
        }

        for (char ch: t) {
            hash[ch]--;

            if (hash[ch] < 0) return false;
        }

        return true;
    }
};

```
