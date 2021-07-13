# https://www.youtube.com/watch?v=KuE_Cn3xhxI&ab_channel=TECHDOSE
class Solution:
    def checkValidString(self, s: str) -> bool:
        star=[]
        opening=[]
        for i in range(len(s)):
            if s[i]==")":
                if len(opening)>0:
                    opening.pop()
                elif len(star)>0:
                    star.pop()
                else:
                    return False                
            elif s[i]=="(":
                opening.append(i)
            else:
                star.append(i)
               
        while len(opening)>0:
                c1=opening.pop()
                if len(star)>0:
                    c2=star.pop()
                    if c1>c2:
                        return False
                else:
                    return False
        return True    
            
                    
            
                
            
            
            
        
        
                    


                
