# [383. Ransom Note](https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150)

Implement the `RandomizedSet` class:

Given two strings `ransomNote` and `magazine`, return `true` _if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise._

Each letter in `magazine` can only be used once in `ransomNote`.

## Example 1:

```

Input: ransomNote = "a", magazine = "b"
Output: false

```

## Example 2:

```

Input: ransomNote = "aa", magazine = "ab"
Output: false

```

## Example 3:

```

Input: ransomNote = "aa", magazine = "aab"
Output: true

```

## Constraints:

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Code

**Hash**

```python

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashNote = {}
        hashMagazine = {}

        for i in ransomNote:
            c = hashNote.get(i, 0)
            hashNote[i] = c + 1

        for i in magazine:
            c = hashMagazine.get(i, 0)
            hashMagazine[i] = c + 1

        for i in ransomNote:
            if hashNote.get(i, 0) > hashMagazine.get(i, 0):
                return False

        return True

```

**Assotiated array**

```python

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        BOUND = ord('a')

        if len(ransomNote) > len(magazine):
            return False

        counter = [0] * 26

        for i in magazine:
            counter[ord(i) - BOUND] += 1

        for i in ransomNote:
            if counter[ord(i) - BOUND] == 0:
                return False
            counter[ord(i) - BOUND] -= 1

        return True

```

```java

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int n = magazine.length();
        int m = ransomNote.length();
        if (m > n) {
            return false;
        }

        int[] counter = new int[26];

        for (int i = 0; i < n; i++) {
            char c = magazine.charAt(i);
            counter[c - 'a']++;
        }

        for (int i = 0; i < m; i++) {
            char c = ransomNote.charAt(i);
            if (counter[c - 'a'] == 0) {
                return false;
            }
            counter[c - 'a']--;
        }

        return true;
    }
}

```
