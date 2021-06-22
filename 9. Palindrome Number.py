class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=str(x)
        st_inv=st.inverse()
        if st==st_inv:
            return True
        else:
            return False
            
