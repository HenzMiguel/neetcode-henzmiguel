class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        row = []
        
        for i in range(numRows):
            
            row.insert(0,1)

            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]

            res.append(row.copy())
        return res
            