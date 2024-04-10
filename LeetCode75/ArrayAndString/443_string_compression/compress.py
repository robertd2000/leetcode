class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        pos = 0
        count = 0
        res = []

        for rigth in range(len(chars) + 1):
            if  rigth >= len(chars) or chars[left] != chars[rigth]:
                chars[pos] = chars[left]
                res.append(chars[left])
                
                pos += 1
                v = list(str(count))
                if count > 1:
                    for j in v:
                        res.append(j)
                        chars[pos] = j
                        pos += 1
                count = 0
                left = rigth
            count += 1

        return len(res)
            
