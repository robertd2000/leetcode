class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        BOUND = ord('a')

        if len(ransomNote) > len(magazine):
            return False
        
        counter = [0] * 26

        for i in magazine:
            counter[ord(i) - BOUND] += 1

        for i in ransomNote:
            if counter[ord(i) - BOUND] == 0:
                return False
            counter[ord(i) - BOUND] -= 1
            
        return True