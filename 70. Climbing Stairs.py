class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
                return 1        
        arr=[1]*(n+1)                  
        for i in range (2,n+1):
            arr[i]=arr[i-1]+arr[i-2]

        return arr[-1]
            
            
            
