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