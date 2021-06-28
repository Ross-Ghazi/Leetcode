#site was done ton check later
class Solution:
    def romanToInt(self, s: str) -> int:
        res=0

        #more 1000
        for i in range(len(s)):
            if s[i]=="M":
                res+=1000
            else:
                break
      
        #more than 500
        for i in range(i,len(s)):
            if s[i]=="D":
                res+=500
            else:
                break    

        #more than 100
        for i in range(i,len(s)):
            if s[i]+s[i+1]=="CD":                
                res+=400
                i=+1
            elif s[i]=="C":
                res+=100              
            else :
                break    


        return res

a= Solution()
print (a.romanToInt("MMD"))
