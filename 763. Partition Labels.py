# no ref was used
# the idea behind leetcode 53 (Merge Intervals) was used here.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
      # first for each letter we put its first appearnace and last appearance in a dic
      dic={}        
        for i,c in enumerate(s):            
            if c in dic:
                l,r=dic[c]
                r=i
                dic[c]=[l,r]
            else:
                dic[c]=[i,i]
        # we do not care about alphabaet or keys we just care about values:   
        li=list(dic.values())
        
        # using the idea behind leetcode 53 (Merge Intervals) we know li is already sorted by first appearance and we will find the merge intervals
        
        res=[li[0]]
        for i in range(1,len(li)):
            l1,r1=res[-1]
            l2,r2=li[i]
            if l2<=r1:
                res[-1][1]=max(r1,r2)
            else:
                res.append([l2,r2])
        # the question is asking for length of each interval
        res1=[]
        for item in res:
            res1.append(item[1]-item[0]+1)
        return res1
        
        
        
        
            
                
        
