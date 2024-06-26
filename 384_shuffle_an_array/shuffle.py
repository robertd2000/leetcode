import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = self.nums[::]
        n = len(shuffled) - 1

        for i in range(n, 0, -1):
            temp = shuffled[i]
            randomIdx = random.randint(0, i)

            shuffled[i] = shuffled[randomIdx]
            shuffled[randomIdx] = temp

        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
