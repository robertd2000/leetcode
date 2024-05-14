class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        BOUND = 97
        n = len(s)
        m = len(t)

        if n != m:
            return False

        counter = [0] * 26

        for i in s:
            counter[ord(i) - BOUND] += 1

        for i in t:
            counter[ord(i) - BOUND] -= 1
            if counter[ord(i) - BOUND] < 0:
                return False

        return True