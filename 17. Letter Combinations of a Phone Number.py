#iterative
class Solutioniterative:
    def letterCombinations(self, digits: str) -> List[str]:          
        if not digits:
            return []
        s=list(digits)
        s.reverse()                
        res=[""]
        dic= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        while s:
            n=s.pop()
            charArray=dic[n]
            newRes=[]           
            for item in res:
                for addon in charArray:  
                    temp=item+addon
                    newRes.append(temp)
            res=newRes
        
        return res
        
            
            
#recursive
class Solutionrecursive:
    def letterCombinations(self, digits: str) -> List[str]:          
        if not digits:
            return []
        dic= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res=[]    
        def rec(index,wordSofar):
            if index==len(digits):
                res.append(wordSofar)
                return
            for c in dic[digits[index]]:
                rec(index+1,wordSofar+c)
        rec(0,"")
        return res
                
                

            
