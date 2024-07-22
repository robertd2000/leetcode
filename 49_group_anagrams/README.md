[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Example 2:**

**Input:** strs = [""]
**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]
**Output:** [["a"]]

**Constraints:**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

```py

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            key = ''.join(sorted(s))
            val = hashMap.get(key, [])
            val.append(s)
            hashMap[key] = val

        return list(hashMap.values())

```

```ts
function groupAnagrams(strs: string[]): string[][] {
  const hashMap = new Map();

  for (let s of strs) {
    const key = s.split("").sort().join("");

    if (hashMap.has(key)) {
      const value = hashMap.get(key);
      value.push(s);
    } else {
      hashMap.set(key, [s]);
    }
  }

  return Array.from(hashMap.values());
}
```
