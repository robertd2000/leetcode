class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        mx = 0
        for i in range(n):
            m = n - citations.index(citations[i], i)
            mx = max(min(m, citations[i]), mx)

        return mx
