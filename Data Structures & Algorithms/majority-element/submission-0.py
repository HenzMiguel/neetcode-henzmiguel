class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        h = {}

        for num in nums:
            h[num] = h.get(num, 0) + 1
        
        m = 0
        res = None
        for key, value in h.items():
            if value > m:
                m = value
                res = key

        return res