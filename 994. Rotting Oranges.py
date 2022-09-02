class Solution:
     def orangesRotting(self, grid: List[List[int]]) -> int:
            que=collections.deque()
            rotten=set()
            fresh=0
            row=len(grid)
            col=len(grid[0])
            time=0
            for r in range(row):
                for c in range(col):
                    if grid[r][c]==1:
                        fresh+=1
                    elif grid[r][c]==2:
                        que.append((r,c))
            
            direction=[(-1,0),(1,0),(0,1),(0,-1)]
            while True:             
                if not fresh:
                    return time
                if not que:
                    return -1                
                for i in range(len(que)):
                    r,c=que.popleft()                                        
                    for x,y in direction:
                        cc=x+c
                        rr=y+r
                        if rr<0 or cc<0 or cc>=col or rr>=row or grid[rr][cc]!=1:
                            continue                     
                        grid[rr][cc]=2
                        fresh-=1
                        que.append((rr,cc))
                time+=1
                
