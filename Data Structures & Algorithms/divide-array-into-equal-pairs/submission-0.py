class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        need = len(nums) / 2
        h = {}
        
        for num in nums:
            h[num] = h.get(num, 0) + 1

        for key in h.keys():
            while h[key] % 2 == 0 and h[key] > 0:
                h[key] -= 2
                need-=1

        return need == 0