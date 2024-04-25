class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        arr = [0] * 128

        for c in s:
            i = ord(c)
            arr[i] = max(arr[i - k : i + k + 1]) + 1
        return max(arr)