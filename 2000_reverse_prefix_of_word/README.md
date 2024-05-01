# [2000. Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=daily-question&envId=2024-05-01)

Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of word that starts at index 0 and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

- For example, if `word = "abcdefd`" and ch = `"d"`, then you should **reverse** the segment that starts at 0 and ends at `3` (**inclusive**). The resulting string will be `"dcbaefd"`.

Return _the resulting string._

## Example 1:

```

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

```

## Example 2:

```

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

```

## Example 3:

```

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

```

## Constraints:

- `1 <= word.length <= 250`
- `word` consists of lowercase English letters.
- `ch` is a lowercase English letter.

# Code

```python

class Solution:
    def reversePrefix(self, word: str, char: str) -> str:
        charIndex = word.find(char)
        pre = word[0:charIndex + 1]
        return pre[::-1] + word[charIndex + 1:]

```

```python

class Solution:
    def reversePrefix(self, word: str, char: str) -> str:
        charIndex = word.find(char)
        res = ''
        l, r = 0, charIndex
        while l <= r:
            res += word[r]
            r-=1
        res +=  word[charIndex + 1:]

        return res
```

```java

class Solution {
    public String reversePrefix(String word, char ch) {
        int charIndex = word.indexOf(ch);
        String pre = new StringBuilder(word.substring(0, charIndex + 1)).reverse().toString();
        return pre + word.substring( charIndex + 1);
    }
}

```

```java

class Solution {
    public String reversePrefix(String word, char ch) {
        int charIndex = word.indexOf(ch);

        String prefix = reverse(word.substring(0, charIndex + 1));
        String postfix = word.substring(charIndex + 1);

        return prefix + postfix;
    }

    private String reverse(String word) {
        String res = "";

        for (int i = word.length() - 1; i >= 0; i--) {
            res += word.charAt(i);
        }

        return res;
    }
}
```

```go

func reversePrefix(word string, ch byte) string {
    chIndex := findIndexInString(word, ch)
    prefix := reverse(word[0:chIndex + 1])
    postfix := word[chIndex + 1:]

    return prefix + postfix
}

func reverse(word string) string {
   var res strings.Builder
    n := len(word)

    for i := n - 1; i >= 0; i-- {
        res.WriteByte(word[i])
    }

    return res.String()
}

func findIndexInString(word string, ch byte) int {
    for i := range word {
        if word[i] == byte(ch) {
            return i
        }
    }

    return -1
}

```
