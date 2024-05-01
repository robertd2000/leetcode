class Solution:
    def reversePrefix(self, word: str, char: str) -> str:
        charIndex = word.find(char)
        pre = word[0:charIndex + 1]
        return pre[::-1] + word[charIndex + 1:]