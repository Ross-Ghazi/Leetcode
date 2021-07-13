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
