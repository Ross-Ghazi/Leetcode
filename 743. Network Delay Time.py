# Dijkstra's algorithm
# https://www.youtube.com/watch?v=EaphyqKU4PQ
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            
            edges=defaultdict(list)        
            for u,v,w in times:
                edges[u].append((w,v))     
            minHeap=[(0,k)]
            seen=set()
            res=0
            while minHeap:
                w1,u1=heapq.heappop(minHeap)
                if u1 in seen:
                    continue
                seen.add(u1) 
                res=max(res,w1)
                for w2,v2 in  edges[u1]:                                
                    if v2 not in seen:
                        heapq.heappush(minHeap,(w1+w2,v2))
            return res if len(seen)==n else -1
                
                            
                                
