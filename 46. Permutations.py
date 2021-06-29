# two different ways
# permute is my own idea and code. for each n in nums that will add we will find all next permutations
# second way permute2 is based on below linl:
# https://www.youtube.com/watch?v=DBLUa6ErLKw&ab_channel=SaiAnishMalla
class Solution:  

    def permute(self, nums):     
        
        def nextperute(nums):
            # works for len nums>=1
            if len(nums)==1:
                return nums
            if len(nums)==2:
                b=nums[::-1]                
                return b
            nums=nums[-1::]+nums[0:-1]
            return nums
        
        
        if len(nums)==1:
                return [nums]
        res=[[nums.pop()]]
        while len(nums)>0:            
            temp=nums.pop()            
            for item in res:             
                item.append(temp)
            res1=res[:] 
            for item in res1:             
                l=len(item)
                b=item[:]
                for i in range(l-1):
                    b=nextperute(b)
                    res.append(b)

    def permute1(self, nums):
        def backtrack(nums, path):
            if len(nums)==0:
                res.append(path)
                return
            for i in range (len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])             
        
        res=[]
        backtrack(nums, [])
        return res
    

    
        
            

        

a=Solution()
print(a.permute([1,2,3]))
print(a.permute1([1,2,3]))
