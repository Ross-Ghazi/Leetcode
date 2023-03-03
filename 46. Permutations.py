import random
import time


# three different solutions: permute is slow but permute_fast and permute_fast_iterative are both eqaully fast.
# permute 0.083 to run
# permute_fast 0.038 to run
# permute_fast_iterative 0.039 to run

class Solution:
    def permute(self, nums) :
        res=[]           
        def dp (rem,path):
            if len(rem)==0:
                    res.append(path)                   
            for i in range(len(rem)):            
                dp(rem[:i]+rem[i+1:] ,[rem[i]]+path)                      
        dp(nums,[])
        return res

    def permute_fast(self, nums):     
        def dp(cur):          
            res=[]  
            if cur==len(nums)-1:   
                     # since this is base case it should have the same format as res wich is [[]]                                   
                    return [[nums[cur]]]               
            temp=dp(cur+1)
            for item in temp:
                # or:
                # res+=[item[:i]+[nums[cur]]+item[i:] for i in range(len(item)+1)]
                # it is impotant to have len(item)+1 because we want [nums[cur]] to be be added even after last elelet of the item   
                # is it also important to note that we add [nums[cur]]
                for x in range(len(item)+1):
                    res+=[item[:x]+[nums[cur]]+item[x:]]
            return res       
        return dp(0)
    
    def permute_fast_iterative(self, nums):   
        res=[[]]
        for n in nums:
            newRes=[]
            for item  in res:            
                for x in range(len(item)+1):
                    newItem=item[:x]+[n]+item[x:]
                    newRes.append(newItem)
            res=newRes
        return res



 
    
        
      


            

nums=[1,2,3]

for i in range(5):
    temp=random.randint(-100,100) 
    nums.append(temp)
nums=list(set(nums))

a=Solution()



start_time = time.time()
temp1=a.permute_fast(nums)
print ("permute_fast", time.time() - start_time, "to run")
start_time = time.time()
temp2=a.permute(nums)
print ("permute", time.time() - start_time, "to run")
start_time = time.time()
temp2=a.permute_fast_iterative(nums)
print ("permute_fast_iterative", time.time() - start_time, "to run")

