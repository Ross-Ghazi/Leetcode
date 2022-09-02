class Solution:
    def trap(self, height: List[int]) -> int:
        #min(max(left),max(right))
        l=0
        r=len(height)-1
        ans=0
        maxLeft=height[l]
        maxRight=height[r]
        while l<=r:            
            if maxLeft<maxRight:                
                area=maxLeft-height[l]
                ans+=area
                l+=1
                maxLeft=max(maxLeft,height[l])              
            
            else:        
                area=maxRight-height[r]
                ans+=area
                r-=1
                maxRight=max(maxRight,height[r])                             
        return ans
            
