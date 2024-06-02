from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        map = {}

        for i in range(len(wall)):
            bricks = 0
            for j in range(len(wall[i]) - 1):
                bricks += wall[i][j]
                value = map.get(bricks, 0)
                map[bricks] = value + 1

        mx = 0

        for i in map.values():
            if i > mx:
                mx = i

        return len(wall) - mx
