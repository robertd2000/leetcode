class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split("."), version2.split("."),
        n1, n2 = len(l1),len(l2)
        n = max(n1, n2)

        for i in range(n):
            v1 = int(l1[i]) if i < n1 else 0
            v2 = int(l2[i]) if i < n2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0