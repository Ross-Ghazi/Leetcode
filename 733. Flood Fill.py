class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or image[r][c] !=start:
                return
            image[r][c]=newColor
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        start=image[sr][sc]
        
        dfs(sr,sc)        
        return image
    
    
    
# this is slower then above solution but space complexity is O(1)    
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        initColor=image[sr][sc]
        def fool(r,c):
            if r>=row or c>=col or c<0 or r<0 or image[r][c]!=initColor:
                return
            image[r][c]=""
            direction=[[0,1],[0,-1],[1,0],[-1,0]]
            for x,y in direction:
                fool(r+y,c+x)
            return
        
        fool(sr,sc)        
        for r in range(row):
            for c in range(col):
                if image[r][c]=="":
                    image[r][c] =color
        return image
        
                
        
