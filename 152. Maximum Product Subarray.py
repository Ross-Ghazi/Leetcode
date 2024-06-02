# No referece was used 
# but here is a link:
# https://www.youtube.com/watch?v=lXVy6YWFcRM&t=69s&ab_channel=NeetCode
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp1=[1]*(len(nums))   
        dp1[0]=nums[0]
        dp2=dp1.copy()
        for i in range(1,len(nums)):
            dp1[i]=max(nums[i],nums[i]*dp1[i-1],nums[i]*dp2[i-1])
            dp2[i]=min(nums[i],nums[i]*dp1[i-1],nums[i]*dp2[i-1])
            
        return max(dp1)
        
# saving memory but no using array.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSub=nums[0]
        minSub=nums[0]
        res=nums[0]     
        for i in range(1,len(nums)):
            temp=maxSub #to save not updated maxSub
            maxSub=max(nums[i],maxSub*nums[i],minSub*nums[i])
            minSub=min(nums[i],temp*nums[i],minSub*nums[i])  #need to times by previous value of minSub
            res=max(res,maxSub)           
        return res



