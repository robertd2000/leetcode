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