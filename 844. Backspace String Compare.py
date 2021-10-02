class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=""
        t1=""
        for c in s:
            if c!="#":
                s1+=c
            else:
                if len(s1)>0:
                    s1=s1[:-1]
            
        for c in t:
            if c!="#":
                t1+=c
            else:
                if len(t1)>0:
                    t1=t1[:-1]  
        if t1==s1:
            return True
        
        return False 
                
                
