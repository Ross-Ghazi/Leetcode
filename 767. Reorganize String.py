class Solution(object):
    def reorganizeString(self, s):
        if len(s)<=1:
            return ""
        d1=collections.defaultdict(int)           
        for i in range(len(s)):
          d1[s[i]]+=1
        max1,max2=0,0   
        c1,c2, res="","",""
        if len(d1)<=1:
            return ""
        while len(d1)>1: 
            max1,max2=0,0   
            c1,c2="",""   
            for key,val in d1.items():
                if val>max1:
                   max1=val
                   c2=c1                   
                   c1=key
                elif val>max2:
                    max2=val
                    c2=key

            res=res+c1+c2         
            d1[c1]-=1
            d1[c2]-=1
            if d1[c2]<=0:
                del d1[c2]
            if d1[c1]<=0:
                del d1[c1]
        if len(d1)==0:
            return res  
        
        freq1=list(d1.values())
        freq=freq1.pop()
        c1=list(d1.keys())
        c=c1.pop()
        
        if freq>1:
            return ""

        if c==res[-1]: 
            return ""
        for i in range(freq):
            res+=c
        return res
        
