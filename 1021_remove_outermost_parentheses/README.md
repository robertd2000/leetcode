# [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/description/)

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: `s = P1 + P2 + ... + Pk`, where `Pi` are primitive valid parentheses strings.

Return `s` after removing the outermost parentheses of every primitive string in the primitive decomposition of `s`.

## Example 1:

```
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
```

## Example 2:

```
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
```

## Example 3:

```
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
```

## Constraints:

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.

# Code

```go

func removeOuterParentheses(s string) string {
	var sb strings.Builder
	op := 0

	for _, c := range s {
		if c == '(' && op > 0 {
			sb.WriteRune(c)
		}

		if c == ')' && op > 1 {
			sb.WriteRune(c)
		}

		if c == '(' {
			op++
		} else {
			op--
		}
	}

	return sb.String()
}

```

```py

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        op = 0

        for c in s:
            if c == "(" and op > 0:
                res.append(c)
            if c == ")" and op > 1:
                res.append(c)
            if c == "(":
                op += 1
            else:
                op -= 1

        return "".join(res)

```
