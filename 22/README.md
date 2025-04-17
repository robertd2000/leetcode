# Generate Parentheses

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

```
Input: n = 1

Output: ["()"]
```

# Example 2:

```
Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
```

You may return the answer in any order.

Constraints:

1 <= n <= 7

```py

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(startN, endN):
            if startN == endN == n:
                res.append(''.join(stack))
                return

            if startN < n:
                stack.append('(')
                backtrack(startN + 1, endN)
                stack.pop()

            if endN < startN:
                stack.append(')')
                backtrack(startN, endN + 1)
                stack.pop()

        backtrack(0, 0)

        return res

```
