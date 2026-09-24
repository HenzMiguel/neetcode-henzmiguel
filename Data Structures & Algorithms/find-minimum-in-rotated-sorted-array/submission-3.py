class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                if m > nums[l]:
                    m = nums[l]
                    break
            
            middle = (l + r) // 2
            
            if nums[l] <= nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
            
            m = min(m, nums[middle])
        return m
            