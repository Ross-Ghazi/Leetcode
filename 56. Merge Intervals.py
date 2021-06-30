# https://www.youtube.com/watch?v=PPGs0gYmhME&ab_channel=SaiAnishMalla
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:            
                res[-1][1]=max(intervals[i][1],res[-1][1])
            else:
                res.append(intervals[i])
        return res
            
