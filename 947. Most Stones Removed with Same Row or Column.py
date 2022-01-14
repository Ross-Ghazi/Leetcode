#dfs
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_coordinate=defaultdict(list)
        y_coordinate=defaultdict(list)
        seen=set()
        count=0
        for index,stone in enumerate(stones):
            i,j=stone            
            x_coordinate[i].append([i,j,index])
            y_coordinate[j].append([i,j,index])
            
            
        def dfs(i,j,index):
            if index in seen:
                return
            seen.add(index)
            
            for stone in x_coordinate[i]:
                ii,jj,iindex=stone
                dfs(ii,jj,iindex)
            for stone in y_coordinate[j]:
                ii,jj,iindex=stone
                dfs(ii,jj,iindex)    
        
            
        
        for index,stone in enumerate(stones):
            i,j=stone                
            if index not in seen:
                dfs(i,j,index)
                count+=1
        return len(stones)-count
                
# union
# class Solution:
#     def removeStones(self, stones):
#         parent={}
#         def find(p):
#                 while p!=parent[p]:
#                     parent[p]=parent[parent[p]]
#                     p=parent[p]                    
#                 return parent[p]

#         def union(p,q):
#                 parent.setdefault(p,p)
#                 parent.setdefault(q,q)
#                 parentP=find(p)
#                 parentQ=find(q)

#                 if parentP==parentQ:
#                     return 

                
#                 parent[parentP]=parentQ
                   
                           
#                 return 1
        
#         for i,j in stones:
#             union(i,~j)
        
#         roots=set()
        
#         for key in parent:
#             root=find(key)
#             roots.add(root)
