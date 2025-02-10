[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

**Example 1:**

**Input:** tokens = ["2","1","+","3","*"]
**Output:** 9
**Explanation:** ((2 + 1) \* 3) = 9

**Example 2:**

**Input:** tokens = ["4","13","5","/","+"]
**Output:** 6
**Explanation:** (4 + (13 / 5)) = 6

**Example 3:**

**Input:** tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**Output:** 22
**Explanation:** ((10 _ (6 / ((9 + 3) _ -11))) + 17) + 5
= ((10 _ (6 / (12 _ -11))) + 17) + 5
= ((10 _ (6 / -132)) + 17) + 5
= ((10 _ 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

**Constraints:**

- `1 <= tokens.length <= 104`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.
  [150. Вычислите обратную польскую нотацию](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Вам дан массив строк `tokens`, который представляет арифметическое выражение в [обратной польской нотации](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Вычислите выражение. Верните _целое число, представляющее значение выражения_.

**Обратите внимание**, что:

- Допустимые операторы: `'+'`, `'-'`, `'*'` и `'/'`.
- Каждый операнд может быть целым числом или другим выражением.
- Деление между двумя целыми числами всегда **обрезает в сторону нуля**.
- Деления на ноль не будет.

- Входные данные представляют собой допустимое арифметическое выражение в обратной польской записи.
- Ответ и все промежуточные вычисления могут быть представлены в виде **32-битного** целого числа.

**Пример 1:**

**Вход:** токены = ["2","1","+","3","*"]
**Выход:** 9
**Пояснение:** ((2 + 1) \* 3) = 9

**Пример 2:**

**Вход:** токены = ["4","13","5","/","+"]
**Выход:** 6
**Пояснение:** (4 + (13 / 5)) = 6

**Пример 3:**

**Вход:** токены = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**Выход:** 22
**Пояснение:** ((10 _ (6 / ((9 + 3) _ -11))) + 17) + 5
= ((10 _ (6 / (12 _ -11))) + 17) + 5
= ((10 _ (6 / -132)) + 17) + 5
= ((10 _ 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

**Ограничения:**

- `1 <= tokens.length <= 104`
- `tokens[i]` является либо оператором: `"+"`, `"-"`, `"*"`, или `"/"`, либо целым числом в диапазоне `[-200, 200]`.

Решение с помощью стека. На каждой итерации проверяем, текущий элемент это оператор или число.

Если оператор, то извлекаем предыдущие 2 числа (так как по правилам польской нотации сначала идут числа-операнды, а потом операторы)- при этом так как мы работаем со стеком, сначала извлекаем второе число (оно будет лежать "сверху"). Далее выполняем математическую операцию с числами и помещаем результат в стек:

```typescript
let b = stack.pop();
let a = stack.pop();
let operator = token;
let value = calculate(a, b, operator);
stack.push(value);
```

Если это число (операнд), то просто переводим его в число и помещаем в стек:

```typescript
stack.push(parseInt(token));
```

В итоге возвращаем последний элемент стека:

```typescript
return stack.pop();
```

Итоговый код:

```typescript
function evalRPN(tokens: string[]): number {
  const stack = [];

  const operations = ["+", "-", "*", "/"];

  for (let token of tokens) {
    if (token.length === 1 && operations.includes(token)) {
      let b = stack.pop();
      let a = stack.pop();
      let operator = token;
      let value = calculate(a, b, operator);
      stack.push(value);
    } else {
      stack.push(parseInt(token));
    }
  }

  return stack.pop();
}

function calculate(a: number, b: number, operator: string): number {
  if (operator === "+") return a + b;
  if (operator === "-") return a - b;
  if (operator === "*") return a * b;
  if (operator === "/") return Math.trunc(a / b);
}
```

```py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                b = stack.pop()
                a = stack.pop()
                operator = token
                res = self.operations(a, b, operator)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()

    def operations(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        return int(a / b)

```

```go

func evalRPN(tokens []string) int {
	stack := []int{}
	operators := map[string]func(int, int) int{
		"+": func(a, b int) int { return a + b },
		"-": func(a, b int) int { return a - b },
		"*": func(a, b int) int { return a * b },
		"/": func(a, b int) int { return a / b },
	}
	for _, token := range tokens {
		if calculate, exist := operators[token]; exist {
			a, b := stack[len(stack)-2], stack[len(stack)-1]
			stack = append(stack[:len(stack)-2], calculate(a, b))
		} else {
			num, _ := strconv.Atoi(token)
			stack = append(stack, num)
		}
	}
	return stack[0]
}

```

```cpp

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        set<string> operations = {"+", "-", "*", "/"};

        for (auto token : tokens) {
            if (operations.find(token) != operations.end()) {
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                int c = calculate(a, b, token);
                stack.push(c);
            } else {
                stack.push(stoi(token));
            }
        }

        return stack.top();
    }

private:
    int calculate(int a, int b, string op) {
        if (op == "+") return a + b;
        if (op == "-") return a - b;
        if (op == "*") return a * b;
        if (op == "/") return a / b;

        return 0;
    }
};

```

```java

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        Set<String> o = new HashSet<>(Arrays.asList("+", "-", "*", "/"));
        for (String i : tokens) {
            if (!o.contains(i))
                stack.push(Integer.valueOf(i));
            else {
                int a = stack.pop(), b = stack.pop();
                if (i.equals("+"))
                    stack.push(a + b);
                else if (i.equals("-"))
                    stack.push(b - a);
                else if (i.equals("*"))
                    stack.push(a * b);
                else
                    stack.push(b / a);
            }
        }
        return stack.peek();
    }
}

```
