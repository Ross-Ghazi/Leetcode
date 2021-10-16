class Solution:
    def removeStones(self, stones):
        parent={}
        def find(p):
                while p!=parent[p]:
                    parent[p]=parent[parent[p]]
                    p=parent[p]                    
                return parent[p]

        def union(p,q):
                parent.setdefault(p,p)
                parent.setdefault(q,q)
                parentP=find(p)
                parentQ=find(q)

                if parentP==parentQ:
                    return 

                
                parent[parentP]=parentQ
                   
                           
                return 1
        
        for i,j in stones:
            union(i,~j)
        
        roots=set()
        
        for key in parent:
            root=find(key)
            roots.add(root)
