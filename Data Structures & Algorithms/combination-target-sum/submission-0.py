class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i, curr, total):
            if i >= len(nums) or total > target:
                return

            if total == target:
                res.append(curr.copy())
                return 
            
            curr.append(nums[i])
            recurse(i, curr, nums[i] + total)

            curr.pop()
            recurse(i + 1, curr, total)

            return
        
        recurse(0, [], 0)

        return res