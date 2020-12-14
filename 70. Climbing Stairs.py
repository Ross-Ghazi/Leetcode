# 70. Climbing Stairs
# Dec 14, 2020
#  Got idea from
# https://www.youtube.com/watch?v=5o-kdjv7FD0&ab_channel=CSDojo
# and
# https://www.youtube.com/watch?v=nqlNzOcnCfs&ab_channel=CSDojo

class Solution:

    # Not efficient
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        return self.climbStairs2(n-1)+self.climbStairs2(n-2)

    # using cash, fast
    from functools import lru_cache
    @lru_cache(None)
    def climbStairs2(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)


    # Manual Hash table
    def climbStairs3(self, n: int) -> int:
        dic={}
        def _climbStairs3(n):
            if n==1: return 1
            if n==2: return 2
            if n in dic:
                return dic[n]
            temp=_climbStairs3(n-1)+_climbStairs3(n-2)
            dic[n]=temp
            return temp
        return _climbStairs3(n)

    # buttom up, iterative
    def climbStairs4(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        case=[0]*n
        case[0]=1
        case[1]=2
        for i in range(2,n):
            case[i]=case[i-1]+case[i-2]
        return case[n-1]




a=Solution()
print(a.climbStairs(5))
print(a.climbStairs2(5))
print(a.climbStairs3(5))
print(a.climbStairs4(5))
