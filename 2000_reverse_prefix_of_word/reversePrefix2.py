class Solution:
    def reversePrefix(self, word: str, char: str) -> str:
        charIndex = word.find(char)
        res = ''
        l, r = 0, charIndex
        while l <= r:
            res += word[r]
            r-=1
        res +=  word[charIndex + 1:]
       
        return res