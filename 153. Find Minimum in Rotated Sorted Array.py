# my own video
#https://www.youtube.com/watch?v=q7ZNEcYpwek
class Solution:
    def findMin(self, nums: List[int]) -> int:        
        l=0
        r=len(nums)-1
        mid=0
        while l<r:  # cannot be <= becasue if r=mid it will be infinite loop         
            mid=(l+r)//2
            if nums[mid]>nums[r]: # > or >= both work
                l=mid+1              
            else:
                r=mid            
        return min(nums[mid],nums[r],nums[l]) # or nums[l] or nums[r] 
    
