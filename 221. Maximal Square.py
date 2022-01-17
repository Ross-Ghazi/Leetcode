class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])        
        dp=[[0]*(col+1) for _ in range(row+1)]
        res=0
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=="1":
                    dp[1+r][1+c]=1+min( dp[1+r][c], dp[r][1+c], dp[r][c])
                    res=max(res,dp[1+r][1+c])
        return res*res
                
        
  
