# the concept is simalr to Dijkstra algorithm, https://github.com/Rouzbeh1797/Leetcode/blob/main/Dijkstra%20algorithm%20to%20findshortest.py
# However, the main difference is we can have only K stops
# here is one refernece:
#https://www.youtube.com/watch?v=IQOG3w4abAg&t=366s&ab_channel=KnowledgeCenter
# it first describe the algorithm and then do it on both c++ amd python
# hoeever he does not have "seen". so his algorithm failed on some cases:
# Using a set for 'seen' will prevent us from finding solutions with a hogher number of stops.
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
                if currentvortex in seen and seen[currentvortex]<=stopes:
                    continue
                seen[currentvortex] = stopes       
                if stopes<=K:
                    for item in adj[currentvortex]:
                        adjvor,adjcost=item
                        heapq.heappush(h,(adjcost+currentcost,adjvor,stopes+1))
        return -1
                
