class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for ch in s:
            if ch == '(':
                cmax += 1
                cmin += 1
            if ch == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if ch == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

