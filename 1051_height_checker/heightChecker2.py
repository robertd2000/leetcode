class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency = [0] * 101

        for height in heights:
            frequency[height] += 1

        result = 0
        current = 0

        for i in range(len(heights)):
            while frequency[current] == 0:
                current += 1

            if current != heights[i]:
                result += 1
            frequency[current] -= 1

        return result