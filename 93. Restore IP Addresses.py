class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def recursive(sofar,index,dots):
            if index==len(s) and dots==4:              
                res.append(sofar[:-1])
            if index==len(s) or dots==4:
                return
            for i in range(index,min(index+3,len(s))):
                temp=s[index:i+1]
                if len(temp)>1 and temp[0]=="0":
                    continue
                if int(temp)<=255:
                    recursive(sofar+temp+".",i+1,dots+1)
        
        recursive("",0,0)
        return res
                
        
        


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
            
                    
