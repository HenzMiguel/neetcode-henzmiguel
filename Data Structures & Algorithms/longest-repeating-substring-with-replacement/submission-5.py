class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        chars = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        longest = 0
        for char in chars:
            l = 0
            bad = 0
            for r, c in enumerate(s):
                if c != char:
                    bad += 1
                while bad > k:
                    if s[l] != char:
                        bad-=1
                    l+=1
                longest = max(longest, r - l + 1)
        return longest