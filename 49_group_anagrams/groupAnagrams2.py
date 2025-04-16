class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            val = h_map.get(key, [])
            val.append(s)
            h_map[key] = val

        res = []

        for i in h_map.values():
            res.append(i)
        return res