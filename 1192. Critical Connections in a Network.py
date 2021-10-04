# made my own video
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
            
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]        
   
        start = 0
        res = []
        cur=0
        seen=set()
        def dfs(node,parent):
            nonlocal cur
            if node  not in seen:
                dfn[node] = cur
                low[node] = cur
                cur+=1
                seen.add(node)               
                for n in graph[node]:
                    if n not in seen:                        
                        dfs(n,node)
                    
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    # parent is None for first Node.
                    l = min(low[i] for i in graph[node]+[low[node]])
                   
                low[node] = l
                
        dfs(0,None)

        
        for v in connections:
            if low[v[0]]>dfn[v[1]] or low[v[1]]>dfn[v[0]]:
            
                res.append(v)
        return res
a=Solution()
n=5
connections = [[0,1],[1,2],[2,0],[1,3]]
a.criticalConnections(n,connections)

