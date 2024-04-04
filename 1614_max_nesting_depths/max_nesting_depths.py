# With stack

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxNesting = 0


        for i in s:
            if i == '(':
                stack.append(i)
            if i == ')':
                stack.pop()

            n = len(stack)

            if n > maxNesting:
                maxNesting = n


        return maxNesting