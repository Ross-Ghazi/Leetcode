class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
    
  
        compl=dict()
        for i in range(len(nums)):
            c=target-nums[i]
            if nums[i] in compl:
                return(i,compl[nums[i]])
            else:
                compl[c]=i
        return 
