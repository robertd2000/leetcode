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
