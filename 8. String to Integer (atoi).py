class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
             return 0
        white_counter=0
        for c in s:
            if c==" ":
                white_counter+=1
            else:
                break
        s=s[white_counter:]
        if s=="":
             return 0
        sign="+"
        if s[0] in "+-":
            sign=s[0]
            s=s[1:]
        res=""
        for c in s:
            if c in "1234567890":
                res+=c
            else:
                break
        if res=="":
            return 0 
        if sign=="+":
            res=int(res)
            if res> (2**31-1):
                res=2**31-1
        else: 
            res=-int(res)
            if res< -(2**31):
                res= -(2**31)
        return res
