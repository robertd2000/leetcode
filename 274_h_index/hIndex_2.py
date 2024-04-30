class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        buckets = [0] * (n + 1)

        for i in citations:
            if i >= n:
                buckets[n] += 1
            else:
                buckets[i] += 1

        
        count = 0

        for i in range(n, 0, -1):
            count += buckets[i]
            if count >= i:
                return i

        return 0
