# https://www.youtube.com/watch?v=sjHuxVwuSgw&ab_channel=RickyCho
class Solution(object):
    def minPathSum(self, grid):      
        row=len(grid)
        col=len(grid[0])
        for r in range(row):
            for c in range(col):
                if r==0:
                    if c==0:
                        pass
                    else:
                        grid[r][c]+= grid[r][c-1]
                elif c==0:
                    grid[r][c]+= grid[r-1][c]
                else:
                     grid[r][c]+= min(grid[r-1][c], grid[r][c-1])
        return grid[-1][-1]
