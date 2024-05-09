class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = 0

        while (i < len(s)): 
            s1 = values[s[i]]
            if (i+1 < len(s)): 
                s2 = values[s[i+1]]
                if (s1 >= s2): 
                    total = total + s1 
                    i = i + 1
                else: 
                    total = total - s1 
                    i = i + 1
            else: 
                total = total + s1 
                i = i + 1
        return total