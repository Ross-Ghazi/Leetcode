# two methods:
# 1.union and find
#2. dfs
from collections import defaultdict
from typing import DefaultDict


def countComponents1(n, edges):   
        parent=[i for i in range(n)]
        rank=[1]*n
        count=n
        def find(p):
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]                    
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
        
        for p,q in edges:
            union(p,q)

        return count

def countComponents2(n, edges):   
    dic=defaultdict(list)
    seen=set()
    ans=0
    def dfs(n):
        if n in seen:
            return
        seen.add(n)
        for i in range (len(dic[n])):
            dfs(dic[n][i])
        return 


    for p,q in edges:
        dic[p].append(q)
        dic[q].append(p)   


    
    for i in range(n):
        if i not in seen:
           
            dfs(i)
            ans+=1
    return ans


n=5
edges=[[0,1],[1,2],[3,4]]
print (countComponents1(n,edges ))
print (countComponents2(n,edges ))
