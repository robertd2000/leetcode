from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        min_len = min([len(i) for i in strs])

        for i in range(min_len):
            if self.is_common_prefix(strs, i + 1):
                res = strs[0][:i + 1]

        return res
        
    def is_common_prefix(self, strs: List[str], n: int) -> bool:
        prefix = strs[0][:n]

        for str in strs:
            if str[:n] != prefix:
                return False

        return True