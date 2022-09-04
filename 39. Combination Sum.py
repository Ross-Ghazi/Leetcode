import random
import time

# two solutions:
# combinationSum and combinationSum_index based  is backtracking: word case time complexity: 2^m
# combinationSum2  is dynamic programming, which is faster :m*m*n

 # I peformed some test combinationSum2 is much faster than combinationSum and ombinationSum_index
 # combinationSum_index is a little bit better than combinationSum

#ref:
# https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
# https://www.youtube.com/watch?v=GBKI9VSKdGg&t=606s 

class Solution: 
    def combinationSum(self, candidates, target):         
        res=[]       
        def dfs(remaning,path,currenSum):           
            if currenSum==target:
                res.append(path)
                return
            if currenSum>target:                
                return
            for i in range(len(remaning)):
                n=remaning[i]
                dfs(remaning[i:],path+[remaning[i]],currenSum+n)                        
        dfs(candidates,[],0)        
        return res
        
    def combinationSum_index(self, candidates, target):
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

   
    def combinationSum2(self, candidates, target: int) :
        # we find dp[] for each number up to the target
        # for example dp[10] is all cases that sum will be 10
        # dp[target] will be all cases  that sum will be target
        dp = [[] for _ in range(target+1)]                    

        for c in candidates:                                 
            for i in range(c, target+1):             #we do not need to check before c as there is no answer
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: 
                    dp[i].append(comb + [c]) # for each combination array of [i-c] we will add [c] for dp[i]
        return dp[-1]
            
                    
target=200
candidates=[]
for i in range(30):
    temp=random.randint(1, 200) 
    candidates.append(temp)

a=Solution()
start_time = time.time()
temp=a.combinationSum(candidates,target)
print ("combinationSum", time.time() - start_time, "to run")
start_time = time.time()
temp=a.combinationSum_index(candidates,target)
print ("combinationSum_index", time.time() - start_time, "to run")
start_time = time.time()
temp=a.combinationSum2(candidates,target)
print ("combinationSum2", time.time() - start_time, "to run")
print("done")
