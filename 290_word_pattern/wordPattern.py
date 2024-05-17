class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h1 = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        for i in range(len(s)):
            if s[i] not in h1:
                h1[s[i]] = pattern[i]
            elif h1[s[i]] != pattern[i]:
                return False

        return True
    