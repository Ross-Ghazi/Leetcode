# 204. Count Primes
# why you do not neet to go more than n**.5:
# https://www.youtube.com/watch?v=fI6kv_GtKlM&ab_channel=NideeshTerapalli
#https://www.youtube.com/watch?v=UMVa5fRKC8I&ab_channel=KevinNaughtonJr.
# https://www.youtube.com/watch?v=fI6kv_GtKlM&ab_channel=NideeshTerapalli


class Solution:
    class Solution:
        def countPrimes(self, n: int) -> int:
            if n <= 2: return 0
            if n == 3: return 1
            list = [1] * n
            for i in range(2, 1 + int(n ** 0.5)):
                j = i
                if list[i] == 1:
                    while i * j < n:
                        list[i * j] = 0
                        j = j + 1
            return (sum(list) - 2)


    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        if n == 3: return 1
        list = [1] * n
        m = int(n ** .5) + 1
        for i in range(2, m):
            if list[i] == 1:
                for j in range(i * i, n, i):
                    list[j] = 0
        return (sum(list) - 2)


a=Solution()
print(a.countPrimes(30))