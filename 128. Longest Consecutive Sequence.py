# ref: https://www.youtube.com/watch?v=P6RZZMu_maU&ab_channel=NeetCode
# on youtube file the for loop is on nums, hower it should be on numsSet to get it faster as there is no duplicat.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)
        res=0
        # for n in nums: //if we loop on array rather than set
        # it will take more time due to duplicates.
        for n in numsSet:
            if (n-1) not in numsSet:
                length=0
                counter=0
                while (n+counter) in numsSet:
                    length+=1
                    counter+=1
                res=max(res,length)
        return res
                
            
