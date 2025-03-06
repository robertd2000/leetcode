class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        freqS = [0] * 26
        freqP = [0] * 26

        n = len(s)
        m = len(p)

        if n < m:
            return res
        
        for i in range(m):
            freqS[ord(s[i]) - ord('a')] += 1
            freqP[ord(p[i]) - ord('a')] += 1

        start = 0
        end = m

        if freqS == freqP:
            res.append(start)
        
        while end < n:
            freqS[ord(s[start]) - ord('a')] -= 1
            freqS[ord(s[end]) - ord('a')] += 1

            if freqS == freqP:
                res.append(start + 1)
            start += 1
            end += 1 

        return res