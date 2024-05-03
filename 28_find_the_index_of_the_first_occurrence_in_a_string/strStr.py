class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        l, r = 0, m - 1

        if m > n:
            return -1

        while l < n:
            if l < n and haystack[l] == needle[0]:
                k = 0
                for i in range(0, m):
                    if i + l < n and haystack[i + l] == needle[i]:
                        k += 1
                if k == m:
                    return l
                l += 1
            else:
                l += 1

        return -1


        
        