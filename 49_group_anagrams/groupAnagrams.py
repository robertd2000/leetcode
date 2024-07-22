class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            key = ''.join(sorted(s))
            val = hashMap.get(key, [])
            val.append(s)
            hashMap[key] = val
        
        return list(hashMap.values())
         