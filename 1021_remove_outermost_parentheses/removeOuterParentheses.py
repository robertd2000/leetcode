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
