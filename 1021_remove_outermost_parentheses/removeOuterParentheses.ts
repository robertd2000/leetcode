function removeOuterParentheses(s: string): string {
  let res: string[] = [];

  let stack: string[] = [];
  let out = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      out++;
    }

    if (s[i] == ")") {
      out--;
    }

    stack.push(s[i]);

    if (out === 0) {
      res.push(...stack.slice(1, stack.length - 1));
      stack = [];
    }
  }

  return res.join("");
}
