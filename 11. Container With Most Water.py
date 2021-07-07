class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while r>l:
            if height[l]<height[r]:
                lowerSide=l
            else:
                lowerSide=r
            volume=(r-l)*height[lowerSide]
            res=max(res,volume)
            if lowerSide==l:
                l+=1
            else:
                r-=1   
        return res
