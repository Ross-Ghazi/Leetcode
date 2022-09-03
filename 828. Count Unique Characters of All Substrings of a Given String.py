class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dic={}
        for i,c in enumerate(s):
            if c in dic:               
                dic[c].append(i)       
            else:
                dic[c]=[-1,i]    #will add -1 and len(s) to the dic
        res=0
        for item in dic.values():
            item.append(len(s))
            for i in range(1,len(item)-1):
                left=item[i]-item[i-1]
                right=item[i+1]-item[i]
                res+=left*right
        return res
    
