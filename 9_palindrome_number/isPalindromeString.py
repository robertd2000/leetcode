class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        xr = x[::-1]

        return x == xr