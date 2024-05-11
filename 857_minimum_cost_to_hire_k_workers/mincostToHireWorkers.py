class Solution:
        def mincostToHireWorkers(self, quality, wage, K):
            workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
            res = float('inf')
            qsum = 0
            heap = []

            for r, q in workers:
                heapq.heappush(heap, -q)
                qsum += q
                if len(heap) > K: qsum += heapq.heappop(heap)
                if len(heap) == K: res = min(res, qsum * r)
                
            return res
        