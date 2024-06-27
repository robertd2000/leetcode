function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  const operations = ["+", "-", "*", "/"];

  for (let token of tokens) {
    if (token.length === 1 && operations.includes(token)) {
      let b = stack.pop() as number;
      let a = stack.pop() as number;
      let operator = token;
      let value = calculate(a, b, operator);
      stack.push(value);
    } else {
      stack.push(parseInt(token));
    }
  }

  return stack.pop() || 0;
}

function calculate(a: number, b: number, operator: string): number {
  if (operator === "+") return a + b;
  if (operator === "-") return a - b;
  if (operator === "*") return a * b;
  if (operator === "/") return Math.trunc(a / b);
  return 0;
}
