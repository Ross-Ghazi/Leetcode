#https://www.youtube.com/watch?v=s-VkcjHqkGI&ab_channel=NeetCode
class Solution:
    def pacificAtlantic(self, heights):
        row=len(heights)
        col=len(heights [0])     
        pac=set()
        atl=set()  
        res=[]
        
        def dfs(r,c,ocean,prev):
            if r<0 or c<0 or c>=col or r>=row:
                return
            if (r,c) in ocean:
                return
            if heights[r][c]<prev:
                return
            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])
            dfs(r,c+1,ocean, heights[r][c])
            
            
        for c in range(col):
                dfs(0,c,pac,heights[0][c])
                dfs(row-1,c,atl,heights[row-1][c])
        for r in range(row):
                dfs(r,0,pac,heights[r][0])
                dfs(r,col-1,atl,heights[r][col-1])  
            
        for r in range(row):
                for c in range(col):
                    if (r,c) in pac and (r,c) in atl:
                        res.append([r,c])
        
        return res
