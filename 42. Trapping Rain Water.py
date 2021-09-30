class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
            
        l=0
        r=len(height)-1
        lMax=height[l]
        rMax=height[r]
        res=0
        while l<r:
            if lMax<=rMax:            
                capacity=min(lMax,rMax)-height[l]
                capacity=max(capacity,0)
                res+=capacity
                l+=1
                lMax=max(lMax,height[l])
            else:
                capacity=min(lMax,rMax)-height[r]
                capacity=max(capacity,0)
                res+=capacity
                r-=1
                rMax=max(rMax,height[r])          
        return res
                
                
                
            
            
