class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        result = []
        for i in range(1,length-1):
            res = []
            for j in range(1,length-1):
                m = max([grid[i-1][j-1],grid[i][j-1],grid[i+1][j-1],grid[i-1][j],grid[i][j],grid[i+1][j],grid[i-1][j+1],grid[i][j+1],grid[i+1][j+1]])
                res.append(m)
            result.append(res)
        return result