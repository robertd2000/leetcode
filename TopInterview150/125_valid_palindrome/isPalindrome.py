class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[' + string.punctuation + ']'
        st = re.sub(pattern, '', s).replace(" ", "").lower()
        n = len(st)

        l, r = 0, n - 1

        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1

        return True