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
