class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        for i in range(n - m + 1):
            if self.isAnagram(s[i : i + m], p):
                res.append(i)

        return res

    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for i in s:
            val = hmap.get(i, 0) + 1
            hmap[i] = val

        for i in t:
            val = hmap.get(i, 0) - 1
            hmap[i] = val

            if val < 0:
                return False

        for i in hmap.values():
            if i > 0:
                return False

        return True
