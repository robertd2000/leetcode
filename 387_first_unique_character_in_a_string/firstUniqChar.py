from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        h_map = defaultdict(int)

        for i in s:
            h_map[i] += 1

        for i in range(len(s)):
            if h_map[s[i]] == 1:
                return i

        return -1