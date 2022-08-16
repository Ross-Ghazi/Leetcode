class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()        
        while n!=1:
            if n in seen:
                return False 
            seen.add(n)
            newN=0
            while n>9:
                newN=newN+(n%10)*(n%10)
                n=n//10
            n=newN+(n%10)*(n%10)                        
        return True
        
        
        
        
