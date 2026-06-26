class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dif = {i for i in range(len(nums) + 1)}
        return set(dif - set(nums)).pop()