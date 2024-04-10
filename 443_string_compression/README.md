# [443. String Compression](https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75)

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

- If the group's length is `1`, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array** `chars`. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array**, return the _new length of the array_.

You must write an algorithm that uses only constant extra space.

## Example 1:

```
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

## Example 2:

```
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
```

## Example 3:

```
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

## Constraints:

- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        pos = 0
        count = 0
        res = []

        for rigth in range(len(chars) + 1):
            if  rigth >= len(chars) or chars[left] != chars[rigth]:
                chars[pos] = chars[left]
                res.append(chars[left])

                pos += 1
                v = list(str(count))
                if count > 1:
                    for j in v:
                        res.append(j)
                        chars[pos] = j
                        pos += 1
                count = 0
                left = rigth
            count += 1

        return len(res)

```
