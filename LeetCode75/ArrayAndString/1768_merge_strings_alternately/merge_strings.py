class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        i, j, k = 0, 0, 0
        n, m = len(word1), len(word2)

        while i < n and j < m:
            if k % 2 == 0:
                res += word1[i]
                i += 1

            if k % 2 == 1:
                res += word2[j]
                j += 1

            k += 1

        while i < n:
            res += word1[i]
            i += 1
            k += 1

        while j < m:
            res += word2[j]
            j += 1
            k += 1

        return res
