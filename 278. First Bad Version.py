class Solution:
    def firstBadVersion(self, n):    
        if isBadVersion(1)==True:
            return 1
        l=2
        r=n
        while l<=r: 
            mid=(l+r)//2           
            res1=isBadVersion(mid-1)
            res2=isBadVersion(mid)                                
            if res1==False and res2==True:
                return mid         
            if res1==False and res2==False:
                l=mid+1
            if res1==True and res2==True:
                r=mid-1
            
            
