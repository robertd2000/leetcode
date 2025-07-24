class Solution:
    def myAtoi(self, s: str) -> int:

        is_negative = False
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        res = ""

        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "+":
                is_negative = False
            elif s[i] == "-":
                is_negative = True
            i += 1

        while i < n and s[i] == "0":
            i += 1

        while i < n and s[i].isnumeric():
            res += s[i]
            i += 1

        if res == "":
            return 0

        m = int(res)

        if is_negative:
            m = -m

        if m > 0 and m >= INT_MAX:
            return INT_MAX

        if m < 0 and m <= INT_MIN:
            return INT_MIN
            
        return m
