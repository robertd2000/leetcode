class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashNote = {}
        hashMagazine = {}

        for i in ransomNote:
            c = hashNote.get(i, 0)
            hashNote[i] = c + 1

        for i in magazine:
            c = hashMagazine.get(i, 0)
            hashMagazine[i] = c + 1

        for i in ransomNote:
            if hashNote.get(i, 0) > hashMagazine.get(i, 0):
                return False

        return True