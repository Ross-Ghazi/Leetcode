class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        row=len(grid)
        col=len(grid[0])
        area=[0]
        def con(r,c):
            if r>=row or r<0 or c>=col or c<0 or grid[r][c]==0:
                return                
            area[0]+=1
            grid[r][c]=0
            con(r+1,c)
            con(r-1,c)
            con(r,c+1)
            con(r,c-1)
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    area[0]=0
                    con(r,c)
                    res=max(res,area[0])
        return res
                
            
