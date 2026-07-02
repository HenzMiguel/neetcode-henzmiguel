class Solution:
    def maxDifference(self, s: str) -> int:
        h = {}
        
        for c in s:
            h[c] = h.get(c, 0) + 1

        a1, a2 = 0, float("inf")

        for value in h.values():
            if value % 2 != 0 and value >= a1:
                a1 = value
            elif value % 2 == 0 and value < a2:
                a2 = value
        
        print(a1, a2)
        return a1 - a2