class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False

        h1 = {}
        h2 = {}

        for i in range(n):
            c1 = h1.get(s[i], 0)
            c2 = h2.get(t[i], 0)

            h1[s[i]] = c1 + 1
            h2[t[i]] = c2 + 1

        return h1 == h2