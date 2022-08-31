class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res=0
        dic=defaultdict(list)
        for  i, c in enumerate(s):
                dic[c].append(i)        
                        
        for arr in dic.values():
            for i,index in enumerate(arr):
                left=0 if i==0 else arr[i-1]+1
                right=len(s)-1 if i==len(arr)-1 else arr[i+1]-1                
                res+=(index-left+1)*(right+1-index)
        return res        
      
            
                    
                        
