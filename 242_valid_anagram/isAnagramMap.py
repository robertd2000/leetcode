class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        for i in s:
            val = hashMap.get(i, 0) + 1
            hashMap[i] = val

        for i in t:
            val = hashMap.get(i, 0) - 1
            hashMap[i] = val

            if val < 0:
                return False
                
        for i in hashMap.values():
            if i > 0:
                return False

        return True

        