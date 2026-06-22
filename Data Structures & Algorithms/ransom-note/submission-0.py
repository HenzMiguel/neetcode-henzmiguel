class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        a, b = {}, {}

        for c in ransomNote:
            a[c] = a.get(c, 0) + 1
        
        for c in magazine:
            b[c] = b.get(c, 0) + 1

        for key in a.keys():
            if b.get(key, 0) < a[key]:
                return False
        return True