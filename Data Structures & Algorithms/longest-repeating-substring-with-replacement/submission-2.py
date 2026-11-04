class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        m = {}
        res = 0
        max_freq = 0

        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            max_freq = max(max_freq, m[s[r]])
            while (r - l + 1) - max_freq > k:
                m[s[l]]-=1
                l+=1
            res = max(res, (r - l + 1))
        return res