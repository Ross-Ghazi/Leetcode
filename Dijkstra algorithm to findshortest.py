# Dijkstra algorithm to find shortest/cheapest path
# ref: https://www.youtube.com/watch?v=XB4MIexjvY0&t=621s&ab_channel=AbdulBari
#ref: https://www.youtube.com/watch?v=Rb0xjNAk5qI&ab_channel=ProgrammingKnowledge
# ref 
import collections
import heapq
def DijkstraSinglepath (flights, src,des):
        # DFS , https://www.youtube.com/watch?v=60RbWlDFsmI&ab_channel=TECHDOSE
        adj=collections.defaultdict(list)
        for start,end, cost in flights:
            adj[start].append((end,cost))     
        h=[] #heap (currentcost of currentvortex from start,currentvortex)
        heapq.heappush(h,(0,src))
        path={}  # set can be used  like: visited=set() but to be similar to all path I used path
        while len(h)!=0:
            currentcost,currentvortex=heapq.heappop(h)
            if currentvortex in path:
               continue 
            path[currentvortex]= currentcost
            if currentvortex==des:               
                return (currentcost)
            for adjvor,adjcost in adj[currentvortex]:
               heapq.heappush(h,(adjcost+currentcost,adjvor)) 
        return -1 #if there is no path return -1

def DijkstraAllpathes (flights, src,des):
        # DFS , https://www.youtube.com/watch?v=60RbWlDFsmI&ab_channel=TECHDOSE
        adj=collections.defaultdict(list)
        for start,end, cost in flights:
            adj[start].append((end,cost))     
        h=[] #heap (currentcost of currentvortex from start,currentvortex)
        heapq.heappush(h,(0,src))
        path={}
        while len(h)!=0:
            currentcost,currentvortex=heapq.heappop(h)
            if currentvortex in path:
               continue 
            path[currentvortex]= currentcost 
            # if currentvortex==des:               
            #     return (currentcost)          
            for adjvor,adjcost in adj[currentvortex]:
               heapq.heappush(h,(adjcost+currentcost,adjvor))         
        #return -1
        return path
        

        


flights=[[1,2,50],[1,4,10],[1,3,45],[2,3,10],[2,4,15],[3,5,30],[4,1,40],[4,5,15],[5,3,35],[5,2,20],[6,5,3]]
print(DijkstraSinglepath(flights,1,6))
print(DijkstraAllpathes(flights,1,6))
