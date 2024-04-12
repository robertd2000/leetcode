class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 1, len(height) - 1

        lmax = height[0]
        rmax = height[-1]
        
        while l <= r:
            
            lmax = max([height[l], lmax])
            rmax = max([height[r], rmax])

            if rmax >= lmax:
                res += lmax - height[l]
                l += 1
            else:
                res += rmax - height[r]
                r-= 1

        return res
