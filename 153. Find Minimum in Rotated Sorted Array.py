class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0 
        r=len(nums)-1
        if r==0:
            return nums[0]
        while True:
            if l>r: 
                return nums[0]
            mid=(l+r)//2
            if mid>0:
                if nums[0]<nums[mid-1] and nums[0]>nums[mid]:
                    return nums[mid]
            else:
                return min(nums[0],nums[1])
               
            if nums[0]<nums[mid]:
                l=mid+1
            else:
                r=mid-1
        
                
                
