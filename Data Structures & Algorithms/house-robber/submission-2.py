def recursion(nums, i, cache):
    if i > len(nums) - 1:
        return 0

    if i in cache:
        return cache[i]

    cache[i] = max(nums[i] + recursion(nums, i + 2, cache), recursion(nums, i + 1, cache))
    return cache[i]

class Solution:
    def rob(self, nums: List[int]) -> int:
        return recursion(nums, 0, {})