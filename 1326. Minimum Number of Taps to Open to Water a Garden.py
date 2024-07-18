class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create a list to track the maximum reach for each position
        max_reach = [0] * (n + 1)

        # Calculate the maximum reach for each tap
        for i in range(len(ranges)):
            # Calculate the leftmost position the tap can reach
            start = max(0, i - ranges[i])
            # Calculate the rightmost position the tap can reach
            end = min(n, i + ranges[i])

            # Update the maximum reach for the leftmost position
            max_reach[start] = max(max_reach[start], end)
        
        res=0
        l=0
        r=0
        prev=-1
        while True:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,max_reach[i])
            if farthest<=r:
                return -1
            l=r+1
            r=farthest            
            res+=1           
            if farthest>=n:
                return res



