class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        

        first = min(prices)
        prices.remove(min(prices))

        second = min(prices)
        prices.remove(min(prices))

        value = money - (first + second)

        return value if value >= 0 else money