#https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        r=[1]*l
        for i in range(l-2,-1,-1):
            for j in range(i+1,l):
                if nums[i]<nums[j]:
                    r[i]=max(r[i], r[j]+1)
        return max(r)
