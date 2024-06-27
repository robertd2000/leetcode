class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        n = len(s)
        l = 0
        maxLength = 0

        for r in range(n):
            if s[r] not in map or map[s[r]] < l:
                map[s[r]] = r
                maxLength = max(maxLength, r - l + 1)
            else:
                l = map[s[r]] + 1
                map[s[r]] = r
            
        return maxLength