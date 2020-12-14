# By Rouzbeh on Dec 12
#62. Unique Paths
# no reference user I just rembered "jaygasht and tarkib". We should have a
#list with (m-1) down* (n-1) right
# Assume m=4 n=3==> we should have m-1 (3) rights and n-1 (3) down in our list. if we had different type of
# rigth and down the result was (m-1+n-1)!
# but they are the same type as "tarkib" so it should be divided by (m-1)! and (n-1)!

from time import time
from functools import lru_cache
def uniquePaths(m, n):
    def factoriel(n):
        if n < 1: return
        if n == 1: return 1
        return n * factoriel(n - 1)

    if m == 1 or n == 1:  return 1
    res = factoriel(m + n - 2)
    temp=(factoriel(m - 1))*(factoriel(n - 1))
    res = res / temp
    return int(res)

# leetcode does not accept it as it take long time to solve unless we put @url_cashe
# based on https://www.youtube.com/channel/UC_xk18oWJ2ineZ1NYYl91Iw/videos   explanaination but not her. totally
# different approach.
@lru_cache
def uniquePaths2(m, n):
    if m == 1 or n == 1:return 1
    return uniquePaths2(m-1,n)+uniquePaths2(m,n-1)

# still not finsihed, https://www.youtube.com/c/chowooick/videos
def uniquePaths3(m, n):
    def dfs(row,col):
        nonlocal count
        if m>row>-1<col<n:
            if row==m-1 and col==n-1:
                count+=1
            dfs(row+1,col)
            dfs(row, col+1)
    count=0
    dfs(0,0)
    return count




a=time()
print(uniquePaths(16,12))
print(time()-a)
a=time()
print(uniquePaths2(16,12))
print(time()-a)
print(uniquePaths3(3,3))
