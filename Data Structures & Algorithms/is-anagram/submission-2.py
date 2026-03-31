class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a, b = {}, {}

        for letter in s:
            a[letter] = 1 + a.get(letter, 0)
        for letter in t:
            b[letter] = 1 + b.get(letter, 0)

        for key in a:
            if b.get(key, 0) != a[key]:
                return False
        return True