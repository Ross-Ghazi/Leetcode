"""
By Rouzbeh
20. Valid Parentheses
Dec 10, 2020
No refernce  was used3
"""


class Solution:
    def isValid(self, s):
        if len(s)%2!=0: return False
        stack=[]
        for c in s:
            if c in"({[": stack.append(c)
            else:
                if len(stack)==0: return False
                a=stack.pop()
                if c==")" and a!="(": return False
                if c == "}" and a != "{": return False
                if c == "]" and a != "[": return False
        if stack != []: return False
        return True

a=Solution()
print(a.isValid("()[]{}"))