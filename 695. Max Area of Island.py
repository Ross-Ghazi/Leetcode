class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        res=0
        
        def dfs(r,c):
            nonlocal res,n
            
            if c<0 or r<0 or c>=col or r>=row or grid[r][c]!=1:
                return
            n+=1            
            grid[r][c]=0                       
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)            
            
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    n=0
                    dfs(r,c)
                    res=max(res,n)                     
        return res
            
