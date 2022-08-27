class Solution:
    def numTrees(self, n: int) -> int:
        #n(4)=
        #n(0)*n(3)+
        #n(1)*n(2)+
        #n(2)*n(1)+
        #n(3)*n(0)
        
        #n(2)=
        #n(0)+n(1)+
        #n(1)+n(0)
        
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1        
        if n<2:
            return 1        
        for i in range(2,n+1):
            temp=0
            for j in range(i):
                left=j
                right=i-j-1
                dp[i]+= dp[left]* dp[right]
        return dp[-1]
