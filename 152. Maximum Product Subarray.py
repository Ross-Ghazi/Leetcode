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
        
