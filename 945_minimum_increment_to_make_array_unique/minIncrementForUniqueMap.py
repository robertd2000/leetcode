from ast import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        root = {}

        def find(x):
            value = find(root[x] + 1) if x in root else x
            root[x] = value

            return root[x]

        return sum(find(num) - num for num in nums)