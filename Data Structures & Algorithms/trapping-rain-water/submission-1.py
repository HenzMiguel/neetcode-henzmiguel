class Solution:
    def trap(self, height: List[int]) -> int:
        su = []
        pre = []

        m = 0
        for h in height:
            su.append(m)
            m = max(m, h)

        m = 0
        for h in reversed(height):
            pre.append(m)
            m = max(m, h)
        pre.reverse()

        total = 0
        for i in range(1, len(height) - 1):
            pilar = min(pre[i], su[i]) - height[i]
            if pilar > 0:
                total+=pilar
        
        return total