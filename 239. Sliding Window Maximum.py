from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k>=len(nums):
            return [max(nums)]
        maxi=deque()        
        res=[]
        l=0
        for i in range(len(nums)):
            while maxi and nums[maxi[-1]]<nums[i]:
                maxi.pop()
            maxi.append(i)          
            if i>=k-1:                
                while maxi and maxi[0]<l:
                    maxi.popleft()
                res+=[nums[maxi[0]]]
                l+=1
        return res
