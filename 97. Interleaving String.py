# using table, start from button, it is good as the indexes are straight forward
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        
        col=len(s1)+1
        row=len(s2)+1
        
        dp=[[False]*col for _ in range(row)]
        dp[-1][-1]=True               
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if  c<col-1 and dp[r][c+1]==True and s1[c]==s3[r+c]:
                    dp[r][c]=True
                if  r<row-1 and dp[r+1][c]==True and s2[r]==s3[r+c]:
                    dp[r][c]=True
                    
        return dp[0][0]
# using table, start from top, indexed need to have -1    
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        
        col=len(s1)+1
        row=len(s2)+1
        
        dp=[[False]*col for _ in range(row)]
        dp[0][0]=True       
       
        
        for r in range(0,row):
            for c in range(0 ,col):
                if  c>0 and dp[r][c-1]==True and s1[c-1]==s3[r+c-1]:
                    dp[r][c]=True
                if  r>0 and dp[r-1][c]==True and s2[r-1]==s3[r+c-1]:
                    dp[r][c]=True        
        return dp[-1][-1]  
    
# recursive with memo    
    class Solution3:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:      
        if len(s1)+len(s2)!=len(s3):
            return False 
        dp={}
        def helper(i,j):        
            if i==len(s1) and j==len(s2):
                return True
            if (i,j) in dp:
                dp[(i,j)]
                return 
            res1=False
            res2=False
            if i<len(s1) and s1[i]==s3[i+j]:
                res1=helper(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                res2=helper(i,j+1)
            dp[(i,j)]=res1 or res2
            return (res1 or res2)
        
        return helper(0,0)
        
    
