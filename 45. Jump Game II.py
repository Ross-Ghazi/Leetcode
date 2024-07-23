class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        res=0
        while r<len(nums)-1:  # if we are on last element len(nums)-1:), we are done, we do not need to go to loop
            farthest=0
            for i in range(l,r+1):
               farthest=max(farthest,i+nums[i]) 
            res+=1
            l=r+1
            r=farthest
        return res
