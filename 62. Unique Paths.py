class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        col=m
        row=n
        grid=[[1]*col for _ in range(row)]
        
        for r in range(row-1-1,-1,-1):
            for c in range(col-1-1,-1,-1):
                grid[r][c]=grid[r+1][c]+grid[r][c+1]
        return grid[0][0]
        
