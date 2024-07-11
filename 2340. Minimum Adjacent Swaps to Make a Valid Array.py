class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:      
        mini=min(nums)
        minIndex=nums.index(mini)
        nums=[nums[minIndex]]+nums[:minIndex]+nums[minIndex+1:]
        nums=nums[::-1]
        maxi=max(nums)
        maxIndex=nums.index(maxi)
        return maxIndex+minIndex


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:      
        maxi=max(nums)
        mini=min(nums)
        for minIndex in range(len(nums)):
            if nums[minIndex]==mini:
                break      
        for maxIndex in range(len(nums)-1,-1,-1):
            if nums[maxIndex]==maxi:
                break  
        res=minIndex+(len(nums)-1-maxIndex)
        if maxIndex<minIndex:
            res-=1     
        return res
