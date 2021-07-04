class Solution(object):
    def numIslands(self, grid):
        row=len(grid)
        col=len(grid[0])
        count=0
        def search(r,c):
            if r<0 or c<0 or c>=col or r>=row:
                return
            
            if grid[r][c]!="1":
                return                       
            grid[r][c]="2"
            search(r+1,c)
            search(r-1,c)
            search(r,c+1)
            search(r,c-1)                        
            
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":                  
                        search(r,c)
                        count+=1
        return count
