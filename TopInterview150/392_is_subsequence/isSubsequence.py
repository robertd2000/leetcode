class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return False
        if n == 0:
            return True

        j = 0

        for i in range(m):
            if j < n and s[j] == t[i]:
                j += 1
        
        return j == n