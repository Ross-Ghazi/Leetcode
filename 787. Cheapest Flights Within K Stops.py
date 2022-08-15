#  Bellman Ford or Dijkstra
#  Dijkstra (bases on 743, modified to have k stop)
# https://github.com/RossGhazi/Leetcode/blob/main/743.%20Network%20Delay%20Time.py
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges=defaultdict(list)
        for s,d,p in flights:
            edges[s].append((p,d))
        minHeap=[(0,src,k+1)]
        seen=set()
        res=0
        while minHeap:               
            w1,u1,k=heapq.heappop(minHeap)
            if u1 in seen:
                continue                
            res=max(res,w1)
            if u1==dst:
                return res
            seen.add(u1)
            if k>0:
                for w2,u2 in edges[u1]:
                    if u2 not in seen:
                        heapq.heappush(minHeap,(w2+w1,u2,k-1))
                       
                        
                        
#  Bellman Ford 
# https://www.youtube.com/watch?v=5eIK3zUdYmE&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=23
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("INF")]*n
        prices[src]=0
        
        for i in range(k+1):
            tempPrices=prices[:]            
            for s,d,p in flights:
                tempPrices[d]=min(tempPrices[d], prices[s]+p)
            prices=tempPrices[:]
            print(prices)
        if prices[dst] == float("INF"):
            return -1
        return prices[dst]
        

            
