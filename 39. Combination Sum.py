# https://www.youtube.com/watch?v=qs1-iEla-5M&ab_channel=SaiAnishMalla
class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]   
        def backtrack(path,index,currentSum):
            if currentSum==target:
                res.append(path[:])
                return
            if currentSum>target:
                return
            for i in range(index,len(candidates)):                  
                backtrack(path+[candidates[i]],i,currentSum+candidates[i])
        backtrack([],0,0)
        return res
            res=[]
        #----------------second method, for loop is different way
        def backtracking(nums,path, currentSum):
            if currentSum>target:
                return
            if currentSum==target:
                res.append(path)
            
            for i,n in enumerate (nums):
                backtracking(nums[i:],path+[n], currentSum+n)        
        backtracking (candidates, [], 0)          
        return res
    
    
a=Solution()  
print(a.combinationSum([2,3,6,7],7))
