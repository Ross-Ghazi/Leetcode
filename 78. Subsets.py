# both have the same result and about the same time

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:      
        # method 1 
        res=[[]]
        for i, n in enumerate(nums):                     
            for i in range(len(res)):
                temp=res[i][:]
                temp.append(n)
                res.append(temp)
        return res
        
        # method 2
        # faster, no nooed for memoization 
            res=[]
            subset=[]
            def dfs(i):
                if i>=len(nums):
                    res.append(subset.copy())
                    return
                
                dfs(i+1)           
    
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()

            dfs(0)
            return res
        
            
            
