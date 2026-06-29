class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = max(nums)

        for i in range(n + 1):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count+=1
            print(count, i)
            if count == i:
                return i

        return -1

