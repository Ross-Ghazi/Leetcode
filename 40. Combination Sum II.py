# my onw video
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:       
        #Reverse Sorting will help here : We hit the cases where the target is exceeded first. Thus, prune helps here
        candidates.sort(reverse=True)
        dic={}
        def backtracking(cur,target):                          
                if target<=0: # since threre is no zero,  < wil also work
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

                    
