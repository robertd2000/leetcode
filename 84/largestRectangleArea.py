class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (idx - index) * height)
                start = index
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)


        return max_area