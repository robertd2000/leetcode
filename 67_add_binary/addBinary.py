class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k = len(a)
        m = len(b)
        n = max(k, m)

        a = a[::-1]
        b = b[::-1]

        res = ""
        carry = 0

        for i in range(n):
            valA = int(a[i]) if i < k else 0
            valB = int(b[i]) if i < m else 0

            total = valA + valB + carry
            val = total % 2

            res = str(val) + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res