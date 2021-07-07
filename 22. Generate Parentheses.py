# no ref was used
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:     
        
        def helper (sofar,num):
            path=[]
            if num/2>n:              
                return sofar            
            for item in sofar:
                if item.count("(")<n:
                    path.append(item+"(")
                if item.count("(")> item.count(")"):
                    path.append(item+")")
            
            return helper(path,num+1)           
                    
            
        
        return helper("(",2)    
