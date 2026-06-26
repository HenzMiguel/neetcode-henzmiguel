class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dif = {i for i in range(len(nums) + 1)}
        res = dif - set(nums)
        return res.pop()