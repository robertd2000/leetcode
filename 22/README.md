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

```java

public class Solution {
    private void backtrack(int openN, int closedN, int n, List<String> res, StringBuilder stack) {
        if (openN == closedN && openN == n) {
            res.add(stack.toString());
            return;
        }

        if (openN < n) {
            stack.append('(');
            backtrack(openN + 1, closedN, n, res, stack);
            stack.deleteCharAt(stack.length() - 1);
        }
        if (closedN < openN) {
            stack.append(')');
            backtrack(openN, closedN + 1, n, res, stack);
            stack.deleteCharAt(stack.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuilder stack = new StringBuilder();
        backtrack(0, 0, n, res, stack);
        return res;
    }
}

```

```cpp

class Solution {
public:
    void backtrack(int openN, int closedN, int n, vector<string>& res, string& stack) {
        if (openN == closedN && openN == n) {
            res.push_back(stack);
            return;
        }

        if (openN < n) {
            stack += '(';
            backtrack(openN + 1, closedN, n, res, stack);
            stack.pop_back();
        }
        if (closedN < openN) {
            stack += ')';
            backtrack(openN, closedN + 1, n, res, stack);
            stack.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string stack;
        backtrack(0, 0, n, res, stack);
        return res;
    }
};

```
