class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]   
        def dp (rem,path):
            if len(rem)==0:
                    res.append(path)                   
            for i in range(len(rem)):            
                dp(rem[:i]+rem[i+1:] ,path+[rem[i]])
        dp(nums,[])
        return res
    
    def permute_fast(self, nums):     
        def dp(cur):          
            res=[]  
            if cur==len(nums)-1:                                      
                    return [[nums[cur]]]               
            temp=dp(cur+1)
            for item in temp:
                # or:
                # res+=[item[:i]+[nums[cur]]+item[i:] for i in range(len(item)+1)]
                # it is impotant to have len(item)+1 because we want [nums[cur]] to be be added even after last elelet of the item               
                for x in range(len(item)+1):
                    res+=[item[:x]+[nums[cur]]+item[x:]]
            return res       
        return dp(0)
