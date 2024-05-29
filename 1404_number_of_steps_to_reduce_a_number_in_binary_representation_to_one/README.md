# [1404. Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2024-05-29)

Given the binary representation of an integer as a string `s`, return _the number of steps to reduce it to `1` under the following rules:_

- If the current number is even, you have to divide it by `2`.
- If the current number is odd, you have to add `1` to it.

It is guaranteed that you can always reach one for all test cases.

## Example 1:

```

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.

```

## Example 2:

```

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

```

## Example 3:

```

Input: s = "1"
Output: 0

```

## Constraints:

- `1 <= s.length <= 500`
- `s` consists of characters `'0'` or `'1'`
- `s[0] == '1'`

# Code

```python

class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            if int(s[l]) + carry == 0:
                carry = 0
                count += 1
            elif int(s[l]) + carry == 2:
                carry = 1
                count += 1
            else:
                carry = 1
                count += 2
            l -= 1
        if carry == 1:
            count += 1
        return count

```

```java

class Solution {
    public int numSteps(String s) {
        int res = 0, carry = 0;
        for (int i = s.length() - 1; i > 0; --i) {
            ++res;
            if (s.charAt(i) - '0' + carry == 1) {
                carry = 1;
                ++res;
            }
        }
        return res + carry;
    }
}

```
