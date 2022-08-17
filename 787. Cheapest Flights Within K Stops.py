#  Bellman Ford or Dijkstra
#  Dijkstra (bases on 743, modified to have k stop)
# https://github.com/RossGhazi/Leetcode/blob/main/743.%20Network%20Delay%20Time.py
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for s,d,p in flights:
            adj[s].append((d,p))
        
        # Heap=[(prcie,stopes, node)]
        H=[(0,0,src)]
        seen={}
        
        while len(H)>0:
            price,stopes,node= heapq.heappop(H)
            
            if node==dst:
                return price
            
            if stopes>k:
                continue                
            if node in seen and seen[node]<stopes:
                continue
            
            seen[node]=stopes
            
            for adjnode,adjcost in adj[node]:
                heapq.heappush(H,(price+adjcost,stopes+1, adjnode))
            
        return -1
        
                       
                        
                        
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
        

            
