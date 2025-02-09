# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Example 1:

```

Input: s = "()"

Output: true

```

## Example 2:

```

Input: s = "()[]{}"

Output: true

```

## Example 3:

```

Input: s = "(]"

Output: false

```

## Example 4:

```

Input: s = "([])"

Output: true

```

## Constraints:

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

# Code

```python

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for i in s:
            if i in parentheses:
                if stack and stack[-1] == parentheses[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) > 0:
            return False

        return True

```

```ts
function isValid(s: string): boolean {
  const characters = ["{", "(", "["];

  const stack = [];

  for (let i of s) {
    if (characters.includes(i)) {
      stack.push(i);
    } else {
      if (stack.length > 0) {
        let last = stack.pop();
        if (last === "{" && i !== "}") return false;
        if (last === "(" && i !== ")") return false;
        if (last === "[" && i !== "]") return false;
      } else {
        return false;
      }
    }
  }

  if (stack.length > 0) return false;

  return true;
}
```

```java

class Solution {
    public boolean isValid(String s) {
        Character[] values = { '(', '[', '{' };
        List<Character> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Arrays.asList(values).contains(c)) {
                stack.add(c);
            } else {
                if (stack.size() == 0) {
                    return false;
                } else {
                    Character current = stack.remove(stack.size() - 1);

                    if (current == '(' && c != ')') {
                        return false;
                    } else if (current == '[' && c != ']') {
                        return false;
                    }
                    if (current == '{' && c != '}') {
                        return false;
                    }
                }
            }
        }

        if (stack.size() > 0) {
            return false;
        }

        return true;
    }
}

```

```go

func isValid(s string) bool {
	var stack []rune
	p := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	for _, i := range s {
		if v, ok := p[i]; ok == true {
			if len(stack) > 0 && stack[len(stack)-1] == v {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, i)
		}
	}

	if len(stack) > 0 {
		return false
	}

	return true
}

```

```cpp

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> map;
        map[')'] = '(';
        map['}'] = '{';
        map[']'] = '[';

        for (auto i : s) {
            if (map.find(i) != map.end()) {
                if (!stack.empty() && stack.top() == map[i]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(i);
            }
        }

        if (!stack.empty())
            return false;

        return true;
    }
};

```
