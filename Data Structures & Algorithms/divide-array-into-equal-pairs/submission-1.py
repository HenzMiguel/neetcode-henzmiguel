class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        need = len(nums) / 2
        h = {}
        
        for num in nums:
            h[num] = h.get(num, 0) + 1

        for key in h.keys():
            if h[key] % 2 != 0:
                return False

        return True