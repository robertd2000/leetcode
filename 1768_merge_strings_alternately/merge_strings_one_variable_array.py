class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        i = 0

        while i < n or i < m:
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])

            i += 1

        return "".join(res)
