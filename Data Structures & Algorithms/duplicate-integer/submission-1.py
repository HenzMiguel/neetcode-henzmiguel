class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_double = set()

        for num in nums:
            if num in has_double:
                return True            
            has_double.add(num)
        return False