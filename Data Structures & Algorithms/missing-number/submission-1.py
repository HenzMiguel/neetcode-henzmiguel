class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        for num in nums:
            if prev is None:
                prev = num
            else:
                if abs(num - prev) != 1:
                    print(num, prev)
                    return prev + 1
                prev = num
        return 0 if nums[0] != 0 else nums[-1] + 1