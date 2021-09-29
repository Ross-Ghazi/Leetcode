class Solution:
    def numTrees(self, n: int) -> int:
        res=[1]*(n+1)
        
        for nodes in range(2,n+1):
            total=0
            
            for cur in range(1,nodes+1):
                left=cur-1
                right=nodes-cur
                total+=res[left]*res[right]
            res[cur]=total
        
        return res[-1]
            
