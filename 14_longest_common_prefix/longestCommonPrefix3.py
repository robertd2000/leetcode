from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        res = []

        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return "".join(res)
            res.append(current_char)

        return "".join(res)
