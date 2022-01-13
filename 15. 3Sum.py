"""

15. 3Sum
Dec 10, 2020

https://www.youtube.com/watch?v=erEHQO0xljc

you can not delete the duplicates of nums because them for example [0,0,0] will be zero.
you cannot break because it does not work for exampel for [[0,0,0,0,0,0]

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            
            while l<r:
                Sum=nums[i]+nums[l]+nums[r]                                
                if Sum==0:                    
                    res.append([nums[i],nums[l],nums[r]]) 
                    print(i,l,r)
                    while l<r and nums[l]==nums[l+1]:
                        l+=1                    
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1
                elif Sum>0:
                    r-=1
                else:
                    l+=1
        return res    

a=Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
