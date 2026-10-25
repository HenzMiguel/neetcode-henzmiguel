class Solution:
    def merge(self, a, b):
        res = []

        while len(a) and len(b):
            if a[0] <= b[0]:
                res.append(a[0])
                a.pop(0)
            else:
                res.append(b[0])
                b.pop(0)
        
        if len(a) > 0:
            res.extend(a)
        elif len(b) > 0:
            res.extend(b)

        return res

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            middle = len(nums) // 2

            left = mergeSort(nums[:middle])
            right = mergeSort(nums[middle:])

            return self.merge(left, right)
        
        nums[:] = mergeSort(nums)
        