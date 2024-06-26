# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150)

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a **palindrome**, or `false` otherwise._

## Example 1:

```

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

## Example 2:

```

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

## Example 3:

```

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

## Constraints:

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

```python

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[' + string.punctuation + ']'
        st = re.sub(pattern, '', s).replace(" ", "").lower()
        n = len(st)

        l, r = 0, n - 1

        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1

        return True

```

```java

class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char charLeft = s.charAt(left);
            char charRight = s.charAt(right);

            if (!Character.isLetterOrDigit(charLeft)) {
                left++;
            } else if (!Character.isLetterOrDigit(charRight)) {
                right--;
            } else {
                if (Character.toLowerCase(charLeft) != Character.toLowerCase(charRight)) {
                    return false;
                }
                left++;
                right--;
            }
        }

        return true;
    }
}

```
