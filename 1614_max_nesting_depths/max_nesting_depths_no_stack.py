class Solution:
    def maxDepth(self, s: str) -> int:
        parenthesesCount = 0
        maxNesting = 0

        for i in s:
            if i == '(':
                parenthesesCount+=1
            if i == ')':
                parenthesesCount-=1
            if parenthesesCount > maxNesting:
                maxNesting = parenthesesCount


        return maxNesting