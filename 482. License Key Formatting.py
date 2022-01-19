class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.upper()
        s="".join(s.split("-"))
               
        left=len(s)%k                   
        s1=s[:left]
        s=s[left:]
        
        if len(s1)>0:
            s1+="-"
        group_number=len(s)//k
        
        s2=""
        print(s) 
        for i in range(group_number):
            start=i*k
            end=(i+1)*(k)        
            temp=s[start:end]
            s2+=temp+"-"           
       
        
        s3=s1[:]+s2[:]
        return s3[:-1]
        
        
            
