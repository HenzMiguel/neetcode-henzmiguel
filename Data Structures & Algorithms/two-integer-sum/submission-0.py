class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ha = {}
        answer = []
        # target = num1 + num2. So target - num1 = num2
        for i in range(len(nums)):
            if nums[i] in ha.keys():
                return [ha[nums[i]], i]             
            ha[target - nums[i]] = i
        
        