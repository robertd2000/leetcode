# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

## Example 1:

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

## Example 2:

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Constraints:

- 1 <= s.length, p.length <= 3 \* 104
- s and p consist of lowercase English letters.

# Code

```py
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        for ch in p: hm[ch] += 1

        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1

        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm:
                hm[s[i+pL]] -= 1

            if all(v == 0 for v in hm.values()):
                res.append(i+1)

        return res

```

```py

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        for i in range(n - m + 1):
            if self.isAnagram(s[i : i + m], p):
                res.append(i)

        return res

    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for i in s:
            val = hmap.get(i, 0) + 1
            hmap[i] = val

        for i in t:
            val = hmap.get(i, 0) - 1
            hmap[i] = val

            if val < 0:
                return False

        for i in hmap.values():
            if i > 0:
                return False

        return True


```
