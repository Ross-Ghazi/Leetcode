# my own video
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
    
    #about two times faster than above
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
    
#     or uaing append
#     class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dp(cur):          
#             res=[]  
#             if cur==len(nums)-1:   
#                     # since this is base case it should have the same format as res wich is [[]]
#                     res.append([nums[cur]])
#                     return res             
#             temp=dp(cur+1)
#             for item in temp:
#                 # or:
#                 # res+=[item[:i]+[nums[cur]]+item[i:] for i in range(len(item)+1)]
#                 # it is impotant to have len(item)+1 because we want [nums[cur]] 
#                 #to be be added even after last elelet of the item   
                
#                 # is it also important to note that we add [nums[cur]]
#                 for x in range(len(item)+1):
#                     res.append(item[:x]+[nums[cur]]+item[x:])
#             return res       
#         return dp(0)
