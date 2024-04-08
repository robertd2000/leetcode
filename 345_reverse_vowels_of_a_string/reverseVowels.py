class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']

        while l < r:
            if word[l].lower() in vowels and word[r].lower() in vowels:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            elif word[l].lower() in vowels and word[r].lower() not in vowels:
                r -= 1
            elif word[l].lower() not in vowels and word[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1

        return "".join(word)

        