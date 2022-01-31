# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        left, right = 0, len(nums)-1              

        while left < right:        
            mid = (left + right) // 2                        
            if nums[mid] > nums[right]:
                left = mid + 1  #we know min is on right side
            else:              
                right = mid      #we know min is on or on left side 

        return nums[left]
                
