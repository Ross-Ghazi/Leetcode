# 242. Valid Anagram
# There are 3 different ways to solve
import collections

    # This is sorting method
def isAnagram1( s: str, t: str) -> bool:

    s=list(s)
    s.sort()
    t=list(t)
    t.sort()
    if t == s:
        return True
    else:
        return False

    # This is hashing method
def isAnagram2( s: str, t: str) -> bool:
    dic1=dic2={}
    for item in s:
        dic1[item]=dic1.get(item,0)+1
    for item in t:
        dic2[item]=dic2.get(item,0)+1
    if dic1==dic2:
        return  True
    else:
        return False


def isAnagram3( s: str, t: str) -> bool:

    dic1=dict(collections.Counter(s))
    dic2=dict(collections.Counter(t))
    if dic1 == dic2:
        return True
    else:
        return False




A=isAnagram1("aa","aa")
print(A)
A=isAnagram2("aa","aa")
print(A)

A=isAnagram3("aa","aa")
print(A)


