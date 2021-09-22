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
                
   

        
        
