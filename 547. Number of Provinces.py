# two methos 1. union and find 2. DFS
# both have the same time complexity
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row=len(isConnected)
        col=row
        count=row
        parent=[i for i in range(row)]
        rank=[1]*row
        def find(p):
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
           
            # if p!=parent[p]:
            #     parent[p]=find(parent[p])
                
            return parent[p]
        
        def union(p,q):
            nonlocal count
            parentP=find(p)
            parentQ=find(q)
            
            if parentP==parentQ:
                return 0
            
            if rank[parentQ]>rank[parentP]:
                parent[parentP]=parentQ
                rank[q]+=rank[p]
            else:
                parent[parentQ]=parentP
                rank[p]+=rank[q]
            
            count-=1
            return 1
        for r in range(row):
            for c in range(col):
                if isConnected[r][c]==1:
                    union(r,c)
        return count
#         N = len(isConnected)       
#         seen=set()
        
#         def dfs(x):
#             for i in range(N):
#                 if (i not in seen) and isConnected[i][x]==1:
#                     seen.add(i)
#                     dfs(i)
                    
#         ans=0        
#         for i in range(N):
#             if i not in seen:
#                 dfs(i)
#                 ans+=1
#         return ans
        
