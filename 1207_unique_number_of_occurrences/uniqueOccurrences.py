from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}

        for i in arr:
            hash[i] = hash.get(i, 0) + 1


        hashValues = len(hash.values())
        hashUnique = len(list(set(hash.values())))

        return hashValues == hashUnique