from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k>=len(nums):
            return [max(nums)]
        res=[]
        q=deque()
        l=0
        for i,n in enumerate(nums):
            while len(q)>0 and q[-1][1]<n:
                q.pop()            
            q.append([i,n])            
            if q[0][0]<i-k:
                q.popleft()           
            if i+1>=k: # we want the sliding winodow length to be k or grater. if index is i., len is i+1
                res.append(q[0][1])
        return res
                
