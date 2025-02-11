[217_contains_duplicate/README.md](https://leetcode.com/problems/basic-calculator/description/)

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

**Example 1:**

Input: s = "1 + 1"
Output: 2

**Example 2:**

Input: s = " 2-1 + 2 "
Output: 3

**Example 3:**

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

**Constraints:**

- 1 <= s.length <= 3 \* 105
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

```py

class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == "+":
                stack.append(v)
            if op == "-":
                stack.append(-v)
            if op == "*":
                stack.append(stack.pop() * v)
            if op == "/":
                stack.append(int(stack.pop() / v))

        stack = []
        sign = "+"
        num = 0
        it = 0

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":
                num, j = self.calculate(s[it + 1 :])
                it = it + j
            elif s[it] == ")":
                update(sign, num)
                return sum(stack), it + 1
            it+= 1

        update(sign, num)
        return sum(stack)


```
