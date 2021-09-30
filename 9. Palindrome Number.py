class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=str(x)
        st_inv=st.inverse()
        if st==st_inv:
            return True
        else:
            return False
            
# or
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
     
        x1=x
        inverse=0
        while True:
            temp=x%10
            inverse=inverse*10+temp
            x=x//10
            if x==0:
                break
        if x1==inverse:
            return True
        else:
            return False 
            
            
