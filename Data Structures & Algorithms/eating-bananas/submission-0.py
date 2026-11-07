class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l, r = 1, max(piles)

        ans = 0
        while l <= r:
            middle = (l + r) // 2

            s = sum([math.ceil(pile / middle) for pile in piles])

            if s <= h:
                r = middle - 1
                ans = middle 
            else:
                l = middle + 1
        return ans