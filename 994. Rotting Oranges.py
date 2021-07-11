# my ows solution
# but got some idead from 
# tps://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        
        time=0
        counter=[0]
      
        # if adjacent cells have fresh orange it will mark them and add to counter
        #we cannot rotten them direcly becasue the for next cells we do not know 
        # if they were already rotten or just got rotten
        def rotten(r0,c0):
            
            if r0+1<row and grid[r0+1][c0]==1:
                grid[r0+1][c0]=""
                counter[0]+=1
            if r0-1>=0 and grid[r0-1][c0]==1:
                grid[r0-1][c0]=""
                counter[0]+=1    

            if c0+1<col and grid[r0][c0+1]==1:
                grid[r0][c0+1]=""
                counter[0]+=1
            if c0-1>=0 and grid[r0][c0-1]==1:
                grid[r0][c0-1]=""
                counter[0]+=1    
                
        
        while True:
            time+=1
            counter[0]=0
            for r in range(row):
                for c in range(col):
                    if grid[r][c]==2:
                        rotten(r,c)
            for r in range(row):
                for c in range(col):
                    # change previously rotten orange so we do not  process them again
                    if grid[r][c]==2:
                        grid[r][c]="1"
                    # make marked oranages rotten
                    if grid[r][c]=="":
                        grid[r][c]=2
                    
            # if there is no new rotten oranage we can exit the loop
            if counter[0]==0:
                break     

        for r in range(row):
             for c in range(col):
                    if grid[r][c]==1:
                        return -1
        # time-1 as we looped one extra time to get counter=0
        return time-1
