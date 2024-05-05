class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, tail = 0, len(s) - 1

        while tail >= 0 and s[tail] == ' ':
            tail-=1
        while tail >= 0 and s[tail] != ' ':
            l += 1
            tail-=1

        return l