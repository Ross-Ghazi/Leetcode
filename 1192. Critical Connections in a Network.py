# made my own video
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
            graph =defaultdict(list)
            for n1,n2 in connections:
                graph[n1].append(n2)
                graph[n2].append(n1)
    
            
            low=[None]*n
            rank=[None]*n
            seen=set()
            currentrank=0
            res=[]
            def dfs(node, parent=None):
                nonlocal currentrank
                if node in seen:
                    return                
                
                rank[node]=currentrank
                low[node]=currentrank
                currentrank+=1
                seen.add(node)
                
                for n in graph[node]:
                    if n not in seen:
                        dfs(n,node)
                low[node]=min([low[n] for n in graph[node] if n!=parent]+[low[node]])
                
            dfs(0)                    
            for n1,n2 in connections:
                if low[n1]>rank[n2] or low[n2]>rank[n1]:
                    res.append([n1,n2])
            return res
    
a=Solution()
n=5
connections = [[0,1],[1,2],[2,0],[1,3]]
a.criticalConnections(n,connections)

