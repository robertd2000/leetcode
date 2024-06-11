class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001

        for i in arr1:
            count[i] += 1

        pos = 0

        for i in arr2:
            while count[i] > 0:
                arr1[pos] = i
                pos += 1
                count[i] -= 1

        for i in range(len(count)):
            while count[i] > 0:
                arr1[pos] = i
                pos += 1
                count[i] -= 1

        return arr1