class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while (l<r): # if l<=r non end loop
            mid=(r+l)//2                    
            if nums[mid]>=nums[r]:# > or >= both work
                l=mid+1    #we know min is on right side              
            else:
                r=mid  #we know min is on or on left side 
        return nums[l]  # both nums[l] and nums[r]  are correct
            
