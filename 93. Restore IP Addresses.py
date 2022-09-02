class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return
        res = []       
        def forwardTacking(s,sofar,dotsofar):
            if dotsofar>4:
                return
            if dotsofar==4 and not s:
                res.append(sofar[:-1])
                return                   
            for i in range(1,min(len(s)+1,4)):
                s1=s[:i]
                s2=s[i:]                
                if s1=="0" or (0<int(s1)<=255 and s1[0]!="0"):
                    forwardTacking(s[i:],sofar+s1+".",dotsofar+1)        
        forwardTacking(s,"",0)
        return res
            
                    
