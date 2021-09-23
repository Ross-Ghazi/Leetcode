# There are different ways to solve it: Dijkstra, Bellman Ford, DFS, BFS

# 1way is based on Dijkstra algorithm
# Here is Dijkstra algorithm itself: https://github.com/Ross-Ghazi/Leetcode/blob/main/Dijkstra%20algorithm%20to%20findshortest.py
# However, the main difference here, is that we can have only K stops
# Here is one refernece on youtube which is wrong:
#https://www.youtube.com/watch?v=IQOG3w4abAg&t=366s&ab_channel=KnowledgeCenter
# it first describe the algorithm and then do it on both c++ amd python
# however he does not have set for "seen". so his algorithm failed on some cases:
# Using a set for 'seen' will prevent us from going through the loops. 
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # DFS , https://www.youtube.com/watch?v=60RbWlDFsmI&ab_channel=TECHDOSE
        adj=defaultdict(list)
        for start,end, cost in flights:
            adj[start].append((end,cost))
            # currentcost,currentvortex,stopes
        h=[(0,src,0)] #heap
        seen={}
        while len(h)>0:   
                currentcost,currentvortex,stopes=heapq.heappop(h)
                if currentvortex==dst:
                    return currentcost
                # regualr Dijkstra algorithm just checked with seen, but here we may see that before (which would have been wither lower cost)
                # but previous visit may had more stops. 
                # we know previous stop was cheaper. If it also had less stops there is not point to continue it.
                # but if we are there with lower number of stops we will push this one also to the heap.
                # so in heap we would have both of them. But we save current number of stops which is the lowest.
                # so in futrure if we visist this note again, we know its price is higher, but we check its number of stops with current number of stops.                
                if currentvortex in seen and seen[currentvortex]<=stopes:
                    continue
                seen[currentvortex] = stopes       
                if stopes<=K:
                    for item in adj[currentvortex]:
                        adjvor,adjcost=item
                        heapq.heappush(h,(adjcost+currentcost,adjvor,stopes+1))
        return -1
    
    
    #------------------------------------------------------------------------------
    # another way to solve it is using modified Bellman Ford algorithim, which is kinf of BFS
    # https://www.youtube.com/watch?v=5eIK3zUdYmE&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=23
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
   

        
        
