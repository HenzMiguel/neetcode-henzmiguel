class Solution:
    def sort(self, a: List[int], b: List[int]) -> List[int]:
        l, r = 0, 0

        res = []
        while l < len(a) and r < len(b):
            if a[l] <= b[r]:
                res.append(a[l])
                l+=1
            else:
                res.append(b[r])
                r+=1
                
        if l >= len(a):
            res.extend(b[r:])
        else:
            res.extend(a[l:])

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        middle = len(nums) // 2

        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])

        res = self.sort(left, right)

        return res