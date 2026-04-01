class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        m = 0
        for r in range(len(prices)):
            difference = prices[r] - prices[l] 
            if difference > m:
                m = difference

            elif prices[r] < prices[l]:
                l = r
                continue
        return m