class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        row_idx = 0
        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else: # < matrix[mid][-1] and > matrix[mid][0]
                row_idx = mid
                break
        
        arr = matrix[row_idx]
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2

            if target < arr[mid]:
                r = mid - 1
            elif target > arr[mid]:
                l = mid + 1
            else:
                return True
        return False