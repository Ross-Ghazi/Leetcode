class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=0
        sum2=0
        for i in range(n):
            sum1+=i
            sum2+=nums[i]
        sum1+=n
        return sum1-sum2
            
