# https://www.youtube.com/watch?v=utBw5FbYswk&ab_channel=GregHogg
# also look at 39, but unlike 39 it is hard to make it completely recursive. 
class Solution:
    def combinationSum2 (self, candidates , target) :       
        #Reverse Sorting will help here : We hit the cases where the target is exceeded first. Thus, prune helps here
        candidates.sort(reverse=True)
        dic={}
        def backtracking(cur,target):                          
                if target<=0: # since there is no zero,  < wil also work
                    return []
                if (cur,target) in dic:
                    return dic[(cur,target)]
                res=[]    
                for i in  range(cur, len(candidates)):
                    if candidates[i] > target:
                        continue
                    if i>cur and candidates[i]==candidates[i-1]:
                        continue                                               
                    if candidates[i] == target:
                        res.append([candidates[i]])
                    temp=backtracking(i+1,target-candidates[i])
                    res += [lst+[candidates[i]] for lst in temp]                
                dic[(cur,target)]=res
                return res 
                    
        
        return backtracking(0,target)
    
    def combinationSum2_basic(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index,target):
            if target<=0:
                return []
            res=[]
            for i in range(index,len(candidates)):
                if i>index and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]==target:
                    res.append([target])
                temp=dfs(i+1,target-candidates[i])
                res+=[item+[candidates[i]] for item in temp]
            return res
        candidates.sort()
        return dfs(0,target)
                
                    
