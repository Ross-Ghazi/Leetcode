def dfs(grid,i,j):
    if  i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
        return
    if grid[i][j]=="0" or grid[i][j]=="2":
         return


    grid[i][j]="2"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i  , j+1)
    dfs(grid, i  , j-1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


n=0
jmax=len(grid[0]) #Horizontal
imax=len(grid)    #Vertical



for i in range(0,imax):
    for j in range(0,jmax):
        if grid[i][j]=="1":
            n+=1
            dfs(grid,i,j)

print(n)