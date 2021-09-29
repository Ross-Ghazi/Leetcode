class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row=len(s1)+1
        col=len(s2)+1
        
        if col+row-2!=len(s3):
            return False       
            
        dp=[[False]*col for _ in range(row)]
        dp[0][0]=True
           
        for r in range(1,row):
            if dp[r-1][0]==True and s1[r-1]==s3[r-1]:               
                dp[r][0]=True
        
        for c in range(1,col):
            if dp[0][c-1]==True and s2[c-1]==s3[c-1]:     
                dp[0][c]=True           
                
                
        for r in range(1,row):
            for c in range(1,col):
                if dp[r][c-1]==True and s2[c-1]==s3[r+c-1]:           
                    dp[r][c]=True
                if dp[r-1][c]==True and s1[r-1]==s3[r+c-1]:             
                    dp[r][c]=True       
        return dp[-1][-1]
    
    # or
    
                                
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row=len(s1)+1
        col=len(s2)+1
        
        if col+row-2!=len(s3):
            return False       
            
        dp=[[False]*col for _ in range(row)]
        dp[0][0]=True                  
                                
        for r in range(0,row):
            for c in range(0,col):
                if c>0 and dp[r][c-1]==True and s2[c-1]==s3[r+c-1]:           
                    dp[r][c]=True
                if r>0 and dp[r-1][c]==True and s1[r-1]==s3[r+c-1]:             
                    dp[r][c]=True       
        return dp[-1][-1]
                             
