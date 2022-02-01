class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=collections.Counter(s)
        h=[]
        for c,n in freq.items():
            h.append([-n,c])
        heapq.heapify(h)
        
        prev=None
        res=""
        
        while prev or h:            
            if prev and not h:               
                return ""                
            
            n,c=heapq.heappop(h)
            n=n*(-1)
            res+=c           
            
            if prev:
                heapq.heappush(h,prev)
                prev=None                
                
            if n!=1:
                n-=1
                prev=[-1*n,c]
        return res
        
