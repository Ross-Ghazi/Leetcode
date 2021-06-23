# By Rouzbeh on June 23, 2021
#62. Unique Paths
# I recorded a video you can watch bere here is hte solutions:
# uniquePaths1: This is comnimation ("jaygasht and tarkib" in farsi). 
# refer to chapter 1 and problem 3.1 mathematics of choice or how to count without counting pdf:
# https://mathsmartinthomas.files.wordpress.com/2018/08/niven-maths-of-choice.pdf
# list with (m-1) down* (n-1) right
# Assume m=4 n=3==> we should have m-1 (3) rights and n-1 (3) down in our list. if we had different type of
# rigth and down the result was (m-1+n-1)!
# but they are the same type as "tarkib" so it should be divided by (m-1)! and (n-1)!
# leetcode does not accept it as it take long time to solve unless we put @url_cashe

# uniquePaths2 using @lru_cache
# uniquePaths3 https://www.youtube.com/watch?v=OL8xlEyqMJE&ab_channel=RickyCho
# uniquePaths4 https://www.youtube.com/watch?v=gp_wfYhjALw&ab_channel=DEEPTITALESRA
# DEEPTI TALESRA defines dp definition is wrong (above link), refer to the first comment or
# my program



from time import time
from functools import lru_cache
def uniquePaths1(m, n):
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

def uniquePaths4(col_end, row_end):
    dp=[[1]*col_end for _ in range(row_end)]
    for row in range (1,len(dp)):
        for col in range(1,len(dp[row])):
            dp[row][col]=...

    return dp[-1][-1]





a=time()
print(uniquePaths(16,12))
print(time()-a)
a=time()
print(uniquePaths2(16,12))
print(time()-a)
a=time()
print(uniquePaths3(16,12))
print(time()-a)
a=time()
print(uniquePaths4(16,12))
print(time()-a)
