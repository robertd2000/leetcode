# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75)

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the _merged string_.

## Example 1:

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

## Example 2:

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
```

## Example 3:

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
```

## Constraints:

```
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
```

# Approach

- Initialize an empty string to store the merged result.
- Traverse both input strings together, picking each character alternately from both strings and appending it to the merged result string.
- Continue the traversal until the end of the longer string is reached.
- Return the merged result string.

# Complexity

- **Time complexity:**
  `O(n)`

# Code

**Traverse**

```python

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        i = 0

        while i < n or i < m:
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])

            i += 1

        return "".join(res)

```

**Two pointers**

```python

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        i, j, k = 0, 0, 0
        n, m = len(word1), len(word2)

        while i < n and j < m:
            if k % 2 == 0:
                res += word1[i]
                i += 1

            if k % 2 == 1:
                res += word2[j]
                j += 1

            k += 1

        while i < n:
            res += word1[i]
            i += 1
            k += 1

        while j < m:
            res += word2[j]
            j += 1
            k += 1

        return res


```

```java

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        int n = word1.length();
        int m = word2.length();

        while (i < n || i < m) {
            if (i < n) {
                result.append(word1.charAt(i));
            }
            if (i < m) {
                result.append(word2.charAt(i));
            }
            i++;
        }

        return result.toString();
    }
}

```
