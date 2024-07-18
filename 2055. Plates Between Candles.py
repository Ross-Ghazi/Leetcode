
# second way of https://leetcode.com/problems/plates-between-candles/solutions/1549018/java-c-python-binary-search-and-o-q-n-solution
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        leftCan = [-1] * n
        for i in range(n):
            if s[i] == '|':
                leftCan[i] = i
            elif i > 0:
                leftCan[i] = leftCan[i - 1]
                        
        rightCan = [-1] * n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                rightCan[i] = i
            elif i < n - 1:
                rightCan[i] = rightCan[i + 1]
        
        canCount = [0] * n
        for i in range(n):
            if s[i] == '|':
                if i == 0:
                    canCount[i] = 1
                else:
                    canCount[i] = canCount[i - 1] + 1
            elif i > 0:
                canCount[i] = canCount[i - 1]
        
        res = []
        for st, end in queries:
            left_candle = rightCan[st]
            right_candle = leftCan[end]
            if right_candle == -1 or left_candle == -1 or right_candle < left_candle:
                res.append(0)
            else:
                temp=right_candle-left_candle-1  # the space between candi
                temp-=canCount[right_candle]-canCount[left_candle]-1 # reduce number of candi
                res.append(temp)
        
        return res
