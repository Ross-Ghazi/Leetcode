class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[] #height,index
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][0]>h:
                height,index=stack.pop()
                width=i-index
                res=max(res, height*width)
                start=index
            stack.append([h,start])
        
        for k in stack:
            height,index=k
            width=len(heights)-index
            res=max(res, height*width)
        return res
            
            
